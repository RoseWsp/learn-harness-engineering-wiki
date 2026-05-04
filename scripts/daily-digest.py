"""
Wiki每日智能摘要推送脚本
- Python: 从log.md提取前一天的所有变更，收集涉及的页面内容
- Claude: 基于实际变更生成知识洞察
- PushPlus: 推送到微信
"""

import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError

# ── 配置 ──────────────────────────────────────────────
WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
PROJECT_DIR = Path(__file__).resolve().parent.parent
SCT_TOKEN = os.environ.get("SCT_TOKEN", "")

# 从项目根目录 .env 文件加载环境变量
_env_file = Path(__file__).resolve().parent.parent / ".env"
if _env_file.exists() and not SCT_TOKEN:
    for line in _env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            if k.strip() == "SCT_TOKEN" and not SCT_TOKEN:
                SCT_TOKEN = v.strip()
SCT_API = "https://sctapi.ftqq.com"


def find_claude_bin() -> str:
    """查找claude可执行文件路径"""
    # 优先用环境变量
    env_path = os.environ.get("CLAUDE_BIN", "")
    if env_path:
        return env_path
    # 用shutil查找
    found = shutil.which("claude")
    if found:
        return found
    return "claude"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


# ── 从log.md提取前一天变更 ────────────────────────────

def parse_log_entries(log_content: str) -> list[dict]:
    """解析log.md，提取所有条目"""
    entries = []
    current = None
    for line in log_content.split("\n"):
        if line.startswith("## ["):
            if current:
                entries.append(current)
            date_match = re.search(r'\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2})\]', line)
            op_match = re.search(r'\] (\w+) \| (.+)', line)
            current = {
                "date": date_match.group(1) if date_match else "",
                "time": date_match.group(2) if date_match else "",
                "op": op_match.group(1) if op_match else "",
                "title": op_match.group(2) if op_match else "",
                "raw": line,
                "details": [],
            }
        elif current:
            current["details"].append(line)
    if current:
        entries.append(current)
    return entries


def extract_page_names(text: str) -> list[str]:
    """从文本中提取所有 [[wikilinks]] 引用的页面名"""
    return list(set(re.findall(r'\[\[([^\]|]+)', text)))


def find_page_path(name: str) -> Path:
    """根据页面名找到文件路径"""
    # 源文件
    p = WIKI_DIR / "sources" / f"{name}.md"
    if p.exists():
        return p
    # wiki根目录
    p = WIKI_DIR / f"{name}.md"
    if p.exists():
        return p
    # 递归搜索
    for md in WIKI_DIR.rglob(f"{name}.md"):
        return md
    return None


def collect_changes(target_date: str = None) -> dict:
    """
    从log.md提取指定日期的所有变更，收集涉及的页面内容。
    target_date: YYYY-MM-DD 格式，默认为昨天
    """
    if target_date is None:
        target_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    log_path = WIKI_DIR / "log.md"
    log_content = read_file(log_path)
    entries = parse_log_entries(log_content)

    # 过滤目标日期的条目
    day_entries = [e for e in entries if e["date"] == target_date]

    if not day_entries:
        return {
            "date": target_date,
            "entries": [],
            "pages": {},
            "page_names": [],
            "summary": f"{target_date} 没有新增内容",
        }

    # 收集所有涉及的页面名
    all_page_names = set()
    for entry in day_entries:
        full_text = entry["raw"] + "\n" + "\n".join(entry["details"])
        names = extract_page_names(full_text)
        all_page_names.update(names)

    # 读取这些页面的内容
    pages_content = {}
    for name in sorted(all_page_names):
        path = find_page_path(name)
        if path:
            content = read_file(path)
            # 截断过长的页面（单页最多3000字，避免上下文爆炸）
            if len(content) > 3000:
                content = content[:3000] + "\n...（已截断）"
            pages_content[name] = content

    # 格式化log条目
    formatted_entries = []
    for entry in day_entries:
        details = "\n".join(entry["details"]).strip()
        formatted_entries.append(f"### [{entry['time']}] {entry['op']} | {entry['title']}\n{details}")

    return {
        "date": target_date,
        "entries": formatted_entries,
        "pages": pages_content,
        "page_names": sorted(all_page_names),
        "summary": f"{target_date} 共{len(day_entries)}条操作，涉及{len(all_page_names)}个页面",
    }


# ── Claude 生成洞察 ───────────────────────────────────

def generate_digest_with_claude(changes: dict) -> str:
    """调用Claude Code，基于前一天的实际变更生成摘要"""

    target_date = changes["date"]

    if not changes["entries"]:
        return f"# Wiki每日摘要 {datetime.now().strftime('%Y-%m-%d')}\n\n昨日（{target_date}）没有新增内容。wiki一切安好，今天可以继续摄入新素材。"

    # 组装变更日志
    log_section = "\n\n".join(changes["entries"])

    # 组装页面内容
    pages_section = ""
    for name, content in changes["pages"].items():
        pages_section += f"\n---\n## 页面：{name}\n\n{content}\n"
    if not pages_section:
        pages_section = "\n（涉及的页面文件未找到）\n"

    prompt = f"""你是一个个人wiki的智能摘要助手。今天是{datetime.now().strftime('%Y-%m-%d')}，你需要基于**昨天（{target_date}）的实际变更**生成一份每日摘要。

## 昨天的操作日志

{log_section}

## 昨天变更涉及的页面内容

{pages_section}

## 你的任务

1. 先读取 wiki/index.md 和 wiki/home.md 了解wiki整体上下文
2. 如果上面的页面内容不够，可以用Read工具读取其他相关页面来补充理解
3. 基于昨天的实际变更，生成每日摘要

## 摘要要求

用中文写，面向wiki的主人。核心原则：**摘要反映昨天发生了什么、新增了什么知识**，而不是泛泛地描述整个wiki。

### 结构

根据昨天的实际变更内容来组织，不要套固定模板。例如：
- 如果昨天ingest了一篇新源文件，就详细介绍这篇源文件的核心内容和它带来的新知识
- 如果昨天digest更新了多个概念页，就逐个说明每个概念页有什么变化
- 如果昨天既ingest又digest，就按逻辑顺序组织
- 如果昨天什么都没做，就简短说"昨天没有新增"

### 写作要求

- 每个新增/变更的页面，要写清楚**具体的内容变化**，不只是"X页面被更新了"
- 把不同页面之间的关联、矛盾、或新发现写出来
- 如果某个变更对wiki的整体理解产生了影响，指出来
- 用 [[wikilinks]] 引用相关页面
- 不要使用emoji
- 整体长度取决于昨天变更的多少，不做人为限制
- 像"写给朋友的一封邮件"，自然、有观点、有判断
- 开头不要写"# Wiki每日摘要"，直接从内容开始"""

    today = datetime.now().strftime("%Y-%m-%d")
    title_line = f"# Wiki每日摘要 {today}\n\n"

    try:
        claude_bin = find_claude_bin()
        print(f"  使用claude: {claude_bin}")

        # 通过stdin传入prompt（避免Windows命令行长度限制）
        result = subprocess.run(
            [claude_bin, "-p", "-", "--output-format", "text"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(PROJECT_DIR),
            timeout=180,
        )

        if result.returncode != 0:
            err = result.stderr or ""
            print(f"Claude调用失败 (exit {result.returncode})")
            print(f"stderr: {err[:500]}")
            return title_line + "生成失败，请手动运行 /digest"

        output = (result.stdout or "").strip()
        return title_line + output

    except subprocess.TimeoutExpired:
        print("Claude调用超时（180秒）")
        return title_line + "生成超时"
    except FileNotFoundError as e:
        print(f"未找到claude命令: {e}")
        print(f"当前PATH: {os.environ.get('PATH', '')[:500]}")
        return title_line + "Claude Code未安装"
    except Exception as e:
        print(f"未知错误: {type(e).__name__}: {e}")
        return title_line + f"生成失败: {e}"


# ── 推送 ─────────────────────────────────────────────

def send_serverchan(title: str, content: str, token: str = "") -> bool:
    """通过Server酱推送到微信"""
    t = token or SCT_TOKEN
    if not t:
        print("错误：未设置 SCT_TOKEN 环境变量")
        print("请到 https://sct.ftqq.com/ 微信扫码登录，获取SendKey")
        print("然后设置环境变量：export SCT_TOKEN=your_sendkey")
        return False

    url = f"{SCT_API}/{t}.send"
    data = json.dumps({
        "title": title,
        "desp": content,
    }).encode("utf-8")

    req = Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if result.get("code") == 0:
                print(f"推送成功！")
                return True
            else:
                print(f"推送失败：{result.get('message', '未知错误')}")
                return False
    except URLError as e:
        print(f"网络错误：{e}")
        return False


# ── 主流程 ────────────────────────────────────────────

def main():
    token = sys.argv[1] if len(sys.argv) > 1 else ""
    # 支持指定日期：python daily-digest.py [token] [2026-05-03]
    target_date = sys.argv[2] if len(sys.argv) > 2 else None

    print("收集昨日wiki变更...")
    changes = collect_changes(target_date)
    print(f"  → {changes['summary']}")

    print("调用Claude生成摘要...")
    digest = generate_digest_with_claude(changes)

    # 保存到wiki
    digest_path = WIKI_DIR / "digest.md"
    digest_path.write_text(digest, encoding="utf-8")
    print(f"摘要已保存到 {digest_path}")

    # 推送到微信
    today = datetime.now().strftime("%m月%d日")
    title = f"Wiki摘要 · {today}"

    sct_token = token or SCT_TOKEN
    if sct_token:
        success = send_serverchan(title, digest, sct_token)
        sys.exit(0 if success else 1)
    else:
        print("\n未配置Server酱token，仅生成摘要未推送。")
        print("1. 到 https://sct.ftqq.com/ 微信扫码登录")
        print("2. 复制你的SendKey")
        print("3. 运行：python daily-digest.py YOUR_SENDKEY")
        print("   或设置环境变量：export SCT_TOKEN=your_sendkey")


if __name__ == "__main__":
    main()
