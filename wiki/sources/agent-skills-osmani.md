# Agent Skills (Addy Osmani)

---
type: article
date: 2026-05-03
author: Addy Osmani
url: https://addyosmani.com/blog/agent-skills/
raw: raw/Agent Skills.md
---

**TL;DR** AI 编码智能体默认跳过高级工程师的"隐形工作"——规格、测试、评审、范围控制、验证证据。Agent Skills 是 Addy Osmani 的尝试：用带退出标准的工作流（skill）把工程纪律重新加回去，让 agent 无法自我说服而绕过。

## 核心论点

Agent 的默认行为是走向"完成"的最短路径——写功能、宣布胜利、继续。它不会问有没有规格说明，不会先写测试，不会考虑信任边界，不会检查 PR 在评审者眼中什么样。这和初级工程师跳过不可见工作的原因一样：奖励信号指向"任务完成"，而不是"任务完成且设计文档也存在"。

高级工程师和初级工程师的核心区别，正是那些不会出现在 diff 里的工作：揭示假设、写规格、拆成可评审的小块、选朴素可靠的设计、留下结果正确的证据、控制改动大小。

## Skill 是什么

Skill 是带 frontmatter 的 markdown 文件，在需要时注入 agent 上下文。它不是参考文档，是工作流：一系列步骤，带检查点，以明确退出标准结束。

**流程优先于散文。工作流优先于参考资料。有退出标准的步骤，优先于没有退出标准的长篇文章。** 这解释了为什么很多"AI rules"仓库在实践中无效——那些规则只是文章。([[process-over-prose]])

## SDLC 映射

20 个 skills 围绕 6 个生命周期阶段组织：

| 阶段 | 命令 | 作用 |
|---|---|---|
| Define | `/spec` | 决定构建什么 |
| Plan | `/plan` | 拆解工作 |
| Build | `/build` | 垂直切片实现 |
| Verify | `/test` | 证明能工作 |
| Review | `/review` | 捕捉漏掉的问题 |
| Ship | `/ship` | 安全交付 |

这就是每个健康工程组织运行的 SDLC。Google 称之为：设计文档 → 评审 → 实现 → 可读性评审 → 发布清单。

## 五个设计原则

1. **流程优先于散文** — 工作流可被 agent 执行，文章不行。([[process-over-prose]])
2. **反合理化表格** — 预判 agent 的自我辩护，提前写下反驳。([[anti-rationalization]])
3. **验证不可协商** — 每个 skill 以具体证据结束。"看起来对"永远不够。([[pass-state-gating]], [[three-layer-termination]])
4. **渐进式披露** — 不一次加载全部 skills，按阶段激活。([[progressive-disclosure]])
5. **范围纪律** — 只碰你被要求碰的东西。([[wip-limit]])

## 反合理化表格

每个 skill 包含一张表，列出 agent 可能用来跳过工作流的借口，配上预写反驳。LLM 极其擅长合理化——生成听起来合理的文字解释为什么这次不需要。反合理化表格是对 agent 还没说出口的谎言提前写好的反驳。([[anti-rationalization]])

## Google 基因

| Skill | 对应实践 |
|---|---|
| api-and-interface-design | Hyrum's Law |
| test-driven-development | 测试金字塔（80/15/5）、Beyoncé Rule、DAMP > DRY |
| code-review-and-quality | ~100 行 PR、Critical/Nit/Optional/FYI 标签 |
| code-simplification | Chesterton's Fence |
| git-workflow-and-versioning | Trunk-based development、atomic commits |
| ci-cd-and-automation | Shift Left、feature flags |
| deprecation-and-migration | Code-as-liability |

## 在 harness 中的位置

Skills 是 [[harness-defined|harness]] 的一层——可复用的工作流片段，渐进式披露到 system prompt 中：

| 层 | 作用 |
|---|---|
| AGENTS.md | 滚动规则手册 |
| hooks | 确定性执行层 |
| tools | agent 可采取的动作 |
| session log | 持久记忆 |
| skills | 高级工程师流程 |

长期运行的 agent 比 10 分钟会话更需要 skills——运行时间越长，每一个捷径的放大效应越大。([[context-anxiety]])

## 三种使用模式

1. **Marketplace 安装** — `/plugin marketplace add addyosmani/agent-skills`
2. **Markdown 放进工具** — 纯 markdown 可用于 Cursor rules、Gemini CLI、任何接受 system prompt 的工具
3. **当规格来读** — 即使不安装，skills 也是关于"如何用 agent 做好工程"的文档化描述

## 与 wiki 的交叉

Osmani 的 SDLC 视角（Define→Plan→Build→Verify→Review→Ship）是**时间维度**，wiki 的五子系统是**结构维度**。两者互补：五子系统保证"有什么机制"，SDLC 保证"什么时候用"。Ralph loop 融合了两者——有隐式生命周期，同时用 plan file 做 state、tests 做 feedback。([[ralph-loop]])

Osmani 的来源更偏 Google 规模化工程经验（Hyrum's Law、Beyoncé Rule、100 行 PR），wiki 的来源更偏 OpenAI/Anthropic 的模型行为研究（[[overconfidence-bias]]、[[context-anxiety]]、[[lost-in-middle-effect]]）。前者解决"人怎么在规模下做对"，后者解决"模型怎么在无人看管时做对"。长期自主运行的 agent 两套经验都需要。

## 传播到 wiki 的页面

Osmani 的 Google 工程实践映射到了多个现有页面：[[e2e-vs-unit-testing]]（Beyoncé Rule、DAMP > DRY）、[[wip-limit]]（100 行 PR、Chesterton's Fence）、[[backpressure-signals]]（Hyrum's Law、Shift Left、code-as-liability）。五条不可协商原则传播到了 [[agents-md]]（"放进任何 AGENTS.md"）和 [[overconfidence-bias]]（"agent 应该 push back"）。Skill 可移植性传播到了 [[agent-native-tooling]]（同一 SKILL.md 跨工具运行）。
