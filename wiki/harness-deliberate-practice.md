# Harness 刻意训练指南

**TL;DR** 码农在 AI 时代面临双重要求：说清楚的能力和代码判断力都不能丢。6 周渐进式训练，每周一个聚焦点，每步都有对照实验。核心目标不是"学会 harness"，而是**把隐含知识变成显性规则、把主观判断变成自动化背压**。

## 从一个码农的真实困境说起

以前说不清楚需求？没关系，自己写代码，跑起来，点两下，能用就行。代码是最终的解释，写的过程本身就是把模糊变清晰的过程。

现在不行了。Agent 不会"自己理解你意思"——它真的按你写的来。你写模糊，它就做模糊。你漏说一个约定，它就不知道那个约定。以前说不清楚的代价是沟通成本，现在说不清楚的代价是返工成本。而且这个返工不是你返工——是 Agent 返工，但它自己不知道要返工，它还觉得自己做完了。这就是 [[premature-victory|过早宣布胜利]]。

最危险的不是"不会用 AI"，而是**用 AI 用久了，代码判断力慢慢退化，自己还不知道**：不看 diff 就接受 Agent 的提交；看了 diff 但看不出问题；看出问题但说不清该怎么改，只能"再跑一轮试试"；架构决策交给 Agent，自己丧失了做 trade-off 的能力。这就像导航用久了，路感就没了。

## Harness 和 Ralph 的关系：道与术

在开始训练之前，先理清概念。

[[harness-defined|Harness Engineering 是学科]]——它回答"为什么 Agent 不靠谱"和"需要哪五个子系统（Instructions、Tools、Environment、State、Feedback）"。它是诊断框架：Agent 失败了，你归因到哪一层，修什么，怎么度量。

[[ralph-loop|Ralph 是一个实现]]——它用最少的机制把 Harness 的核心原则落地了：一个 dumb bash 循环不断重启 Agent，plan 文件作为迭代间唯一共享状态。Ralph 不是 Harness 的替代品或竞争者，它是**一个把 Harness 原则工程化的跑法**。

类比：Harness = 软件工程的"测试很重要""要 CI""要 code review"这些原则。Ralph = 一个具体的 GitHub Actions workflow + 分支保护规则 + PR template。你不会问"GitHub Actions 和软件工程哪个好"——前者是后者的工具化。

而且 Ralph 并没有覆盖 Harness 的全部。比如 Environment 子系统（依赖版本、服务就绪），Ralph 没有特别的机制；[[sprint-contract|Observability]]（冲刺合约、评估量表）Ralph 也只是浅尝。Ralph 最强的地方是 [[progress-md|State]]（plan 文件做交接）和 [[backpressure-signals|Feedback]]（测试做背压），其他子系统靠的是通用的 sandbox 和 AGENTS.md 最佳实践。

但 Ralph 提供了一个核心洞察：**上下文是唯一重要的东西。** 200K token 窗口实际可用约 176K，40-60% 利用率是推理质量的"聪明区"。一轮一个任务 = 100% 聪明区利用。主 Agent 当调度员，[[subagent-scheduling|subagent 干活]]，上游确定性信号 + 下游背压 = 收敛。这些不是抽象原则，是可操作的工程决策。

## 两条线同时拉

AI 时代码农的核心能力是**双轨**的：

**第一条线：说清楚的能力。** 以前这是 nice-to-have，现在是 must-have。[[agents-md|AGENTS.md]]、spec、验收标准——全是"说清楚"的载体。写不好这些，Agent 就是在没有地图的情况下开车。

**第二条线：代码判断力不能丢。** Agent 写了代码，你得能判断它对不对、架构合不合理、有没有隐患。如果你自己代码能力退化了，你就变成外行审内行——看不出问题，只能看测试过没过。但测试只验证你想到的，验证不了你没想到的。

这两条线其实是**同一件事的两面**：能说清楚 = 说明你真的理解了。写不出清晰的 spec，多半是因为你自己也没想清楚。写 AGENTS.md 的过程逼你把隐含知识显性化——这本身就是深度思考。而代码判断力 = 读懂 Agent 产出的能力。每次看 diff，问自己：它为什么这么做？有没有更简单的做法？边界情况考虑了吗？答不上来，就说明你的判断力在这块有缺口。

## 训练原则

1. **对照实验**：每个练习都跑两次——一次没 harness，一次有 harness。量化差距，而不是凭感觉
2. **修 harness，不修代码**：看到问题，先问"harness 哪一层没挡住"，而不是上手改代码。修了代码，下次还犯；修了 harness，下次自动避坑
3. **60 行上限**：[[agents-md|AGENTS.md]] 超过 60 行就砍。[[lost-in-middle-effect|中间的内容会被忽略]]
4. **说清楚才算想清楚**：写不出 spec 的地方，说明你自己也没想清楚。停下来想，别让 Agent 猜

## 第 1 周：说清楚——写 AGENTS.md

**目标**：让一个完全不了解你项目的人（或 Agent）5 分钟内能跑起来、能测试、能提交。

**练习**：

选一个你正在做的项目（不要选太复杂的，选你熟悉的、能 10 分钟讲完的）：

1. 写 `AGENTS.md`，包含：Build & Run、测试命令、项目结构、关键约定
2. **冷启动测试**：开一个新的 Claude 会话，只给 AGENTS.md，不给任何口头提示，让它跑项目、跑测试
3. 记录它来问你的每一个问题——每个问题都是你 AGENTS.md 的缺口
4. 补上缺口，再跑一次冷启动测试，直到它不再问你

**检验标准**：Agent 能独立完成 `安装依赖 → 启动项目 → 跑通测试 → 做一个小修改 → 提交`，全程不问你。

**常见坑**：
- 写了 200 行 AGENTS.md → 砍到 60 行，[[lost-in-middle-effect|中间的内容会被忽略]]
- 只写了"怎么跑"，没写"怎么测试" → 测试命令是背压的入口，必须有
- 写了 changelog 和设计文档 → AGENTS.md 是操作手册，不是历史记录

## 第 2 周：挡住坏代码——加测试背压

**目标**：Agent 提交代码后，有自动化手段挡住坏代码。wiki 原话：**"Feedback has the highest ROI — verification commands are the single most impactful thing you can add."**

**对照实验**：

1. **无背压跑**：让 Agent 实现一个功能（比如加一个新 API 端点），不要求它跑测试，不设任何 gate。观察：它自己跑测试了吗？提交的代码能跑通吗？
2. **有背压跑**：在 AGENTS.md 加粗写"测试必须通过才能提交"，加 pre-commit hook（`npm test && npm run lint && npm run typecheck`），同样的任务再让 Agent 做一次。对比两次产出质量

**量化记录**：
- 无背压：几次提交能跑通？产生了几个 bug？
- 有背压：几次提交能跑通？测试挡住了几个坏提交？

**进阶**：如果你的项目测试覆盖率低，先补**一条 e2e 测试覆盖最关键的 happy path**，而不是追求覆盖率。[[e2e-vs-unit-testing|Unit test 漏组件边界问题]]，一条 e2e 的背压价值 > 20 条 unit test。

## 第 3 周：跨越会话——加状态持久化

**目标**：新会话不问你"上次做到哪了"，它能自己找到答案。

**练习**：

1. 创建 `PROGRESS.md`，记录：当前状态、已完成、下一步、决策记录
2. 用 Agent 做一个需要 2-3 个会话才能完成的功能
3. 每个会话结束时让它更新 PROGRESS.md
4. 下个会话开始时，只让它读 PROGRESS.md，不提供任何额外上下文

**检验标准**：新会话读完 PROGRESS.md 后，能准确说出"上次做到哪了"和"下一步做什么"。

**[[cold-start-test|冷启动五问]]**——新会话必须能回答：
1. 这个项目做什么？
2. 当前状态是什么？
3. 下一步做什么？
4. 有什么阻塞？
5. 关键决策是什么？

答不上来的，就是 PROGRESS.md 的缺口。

## 第 4 周：限定范围——WIP=1 和任务边界

**目标**：Agent 不贪多、不提前宣布胜利。

**对照实验**：

1. **无范围控制**：给 Agent 3 个任务，让它一次做完。观察：它做了几个？每个都做完了吗？有没有半途而废的？
2. **WIP=1**：用 [[feature-list|feature_list]] 跟踪任务状态，明确告诉 Agent"一次只做一个任务，做完标记完成再开始下一个"。同样 3 个任务。对比完成率

**[[pass-state-gating]]** 的练习：在 feature_list 里加一条规则——"只有测试通过才能标记为 pass"。观察 Agent 有没有跳过测试直接标记 pass。如果有，加 [[three-layer-termination|三层验证]]：语法检查 → 单元测试 → e2e 测试，全过才能 pass。

## 第 5 周：跑一次完整 Ralph 循环

**目标**：把前 4 周的 harness 组装成可运行的循环，体会"在循环外观察"的感觉。

**搭建**：

```
项目根目录/
├── AGENTS.md          # 第 1 周写的
├── PROMPT_build.md    # 构建指令
├── IMPLEMENTATION_PLAN.md  # 任务清单
├── PROGRESS.md        # 第 3 周写的
├── feature_list.json  # 第 4 周写的
├── init.sh            # 初始化脚本
└── specs/             # 需求文档
```

**手动跑一轮**（不用 `--dangerously-skip-permissions`）：

1. 开新会话，给 `PROMPT_build.md`
2. 观察 Agent 的每一步：它读 AGENTS.md 了吗？选对任务了吗？跑测试了吗？测试挂了修了吗？更新 PROGRESS.md 了吗？
3. 哪里卡住，就回去修哪一层 harness
4. 重复，直到一轮能完整走通

**观察日志**——每轮结束后记录：

| 观察 | 归因到哪一层 | 怎么修 |
|---|---|---|
| Agent 忘跑测试 | Feedback | AGENTS.md 加粗 / 加 pre-commit hook |
| Agent 选错任务 | State | IMPLEMENTATION_PLAN.md 加优先级 |
| 代码风格不一致 | Instructions | AGENTS.md 加 coding style |
| 重复犯同一个错 | Instructions | AGENTS.md 加"不要 X" |
| 改了 A 坏了 B | Feedback | 补 e2e 测试 |
| 新会话不知道上次做哪了 | State | 检查 PROGRESS.md |

**核心心态**：看到问题，别上手改代码，改 harness。这就是 [[diagnostic-loop]]——归因到层，修，度量。

## 第 6 周：Ablation——拆掉看看什么在撑着

**目标**：验证你建的 harness 里，哪些真的起作用，哪些是摆设。

**Ablation 实验**：

选一个固定任务，用完整 harness 跑一次作为基线。然后逐个拆掉 harness 组件，各跑一次：

| 实验 | 拆掉什么 | 记录什么 |
|---|---|---|
| 完整 harness | 无（基线） | 完成率、耗时、bug 数 |
| 无 AGENTS.md | Instructions 层 | Agent 犯了哪些约定违反？ |
| 无测试背压 | Feedback 层 | 坏代码混进来了几个？ |
| 无 PROGRESS.md | State 层 | 新会话恢复花了多久？ |
| 无 WIP 限制 | Scope 层 | Agent 贪多了吗？提前宣布胜利了吗？ |
| 全拆 | 全部 | 跟完整 harness 差多少？ |

这正是 Anthropic 做过的实验的逻辑：同一个模型，有 harness 和没 harness，产出天差地别。现在你自己亲手验证每一层的贡献。

## 持续训练：日常中的微练习

6 周之后，harness 的骨架有了。但 harness 会腐化——[[harness-rot|AGENTS.md 慢慢过时、测试覆盖漂移、PROGRESS.md 停更]]。日常维护本身就是训练：

- **每次 Agent 犯错** → 问"harness 哪层没挡住" → 修 harness → 记录
- **每周 10 分钟** → 读一遍 AGENTS.md，删掉过时的、补上新增的
- **每次新会话** → 检查 PROGRESS.md 是否准确，不准确就改模板
- **每个新项目** → 从零搭 harness，不用旧项目的模板（每个项目约定不同，模板会骗你）

## 两条线的日常检查

| 说清楚的能力 | 代码判断力 |
|---|---|
| 能写出 Agent 不来问你的 AGENTS.md 吗？ | 看 Agent 的 diff，能 3 句话说清它做了什么吗？ |
| 能写出有明确验收标准的 spec 吗？ | 能看出 Agent 的代码有没有架构问题吗？ |
| 能把隐含约定变成显性规则吗？ | 能判断 Agent 选的实现方案是不是最简单的吗？ |
| PROGRESS.md 写完，新人能接手吗？ | 测试全过了，你还敢说"这代码没问题"吗？ |

两条线任何一条退化，你就从"驾驶 Agent"退化为"被 Agent 驾驶"。

---

[[harness-defined]] · [[agents-md]] · [[e2e-vs-unit-testing]] · [[progress-md]] · [[wip-limit]] · [[pass-state-gating]] · [[three-layer-termination]] · [[diagnostic-loop]] · [[ralph-loop]] · [[subagent-scheduling]] · [[backpressure-signals]] · [[harness-rot]] · [[cold-start-test]] · [[lost-in-middle-effect]] · [[overconfidence-bias]] · [[premature-victory]] · [[anti-rationalization]] · [[process-over-prose]]
