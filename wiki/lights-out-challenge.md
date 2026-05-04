# Lights-Out 挑战：Harness 的终局形态

**TL;DR** 现有 harness 的隐含假设是"人还在循环里"——人读 diff、人审 spec、人做判断。SkipLabs 两篇文章指向一个终局：人不在循环里，信任完全建立在过程上。这不否定 harness，但意味着 harness 的最终形态不是"更好的辅助工具"，而是"让人可以不在场的信任基建"。

## 三层颠覆

### 第一层：代码还需要人读吗？

现有 [[harness-defined|harness 体系]]和 [[harness-deliberate-practice|训练指南]]都隐含一个前提：Agent 写的代码，人得能读懂、能判断。所以训练指南里写"看 Agent 的 diff，能 3 句话说清它做了什么吗？""能看出 Agent 的代码有没有架构问题吗？"

[[codegen-as-compiler-output|SkipLabs 的编译器类比]]说：这个前提是过渡态。就像没人审查编译器的汇编输出一样，当验证基建足够强时，人不需要读懂 Agent 产出的代码。你信任的是测试、类型系统、形式化规格、AI 审 AI 的管道，不是你自己的 diff 阅读能力。

这对"代码判断力"构成了直接挑战：**如果代码判断力的终局是被验证体系替代，那我们训练它的意义是什么？** 是永远需要的核心能力，还是像手写汇编一样会过时的技能？

我的判断：**短期内（2-3 年）代码判断力仍然是必须的**，因为验证基建还没建好。但长期来看，"人读代码"的定位会从**质量门禁**变成**异常排查**——就像今天你读汇编不是为了日常开发，而是为了 debug 编译器 bug。[[harness-deliberate-practice|训练指南]]里的"两条线"不会消失，但权重会变：说清楚的能力（写 spec、写 harness）会越来越重要，代码判断力会从"全部"降级为"底线中的底线"。

### 第二层：AGENTS.md 是不是太原始了？

现有 harness 的 [[agents-md|Instructions 子系统]]核心是 markdown 文件——AGENTS.md、PROMPT_build.md、specs/*.md。这些是自然语言指令。

编译器有类型系统作为"代码执行前的形式化合约"。Agent 对应的东西还是原始的——Prompts 不是 formal spec。TDD、contract testing、design-by-specification 存在，但在 Agent 是代码作者的场景下还不是标准做法。

AGENTS.md 是给 Agent 的"入职手册"。但入职手册不管用的时候，你需要的是**劳动合同**——形式化的、可验证的、机器可执行的合约。

具体升级路径：
- **从自然语言规格 → 形式化规格**：验收标准不只是写"提取 5-10 种主色"，而是写成可机器验证的 contract
- **从"告诉 Agent 怎么做" → "约束 Agent 做什么"**：类型系统约束的不是写作风格，而是代码能做什么、不能做什么
- **从 AI-readable → AI-optimal**：工具、语言、错误信息不再优化人类可读性，而是优化 Agent 可执行性（[[agent-native-tooling]]）

这不是推翻 harness，而是说 **Instructions 层可能需要从 markdown 升级到某种形式化规格层**。当前 markdown 仍然是最实用的载体，但它是过渡态。

### 第三层：测试"够用"的标准要大幅提高

现有 harness 说 [[backpressure-signals|"Feedback 有最高 ROI"]]，测试是背压的核心，"补一条 e2e happy path 就够用"。

SkipLabs 指出一个量化问题：**编译器是确定性的，Agent 不是。** 一个能以 50 倍速率生成"看起来对但实际有微妙错误"的代码的作者，需要比人类作者时代实质性更全面的测试。

"够用"的标准变了：

| | 人类作者 | Agent 作者 |
|---|---|---|
| 犯错速率 | 1x | 50x |
| 错误特征 | 明显的、可直觉发现的 | 微妙的、plausible-but-wrong |
| 测试策略 | happy path + 关键路径 | 需要实质性更全面的覆盖 |
| AI 审 AI | 可选增强 | 一等 CI 基建 |
| 生产监控 | 有则更好 | 必须有——测试没挡住的靠监控捕获 |

[[acceptance-driven-backpressure|验收驱动背压]]的方向是对的——在规划阶段就从验收标准推导测试要求。但标准需要提高：不是"有测试就行"，而是"测试覆盖要能替代人类 code review 作为质量门禁"。

## 哪些被颠覆，哪些站得住

| 现有 harness 原则 | SkipLabs 的挑战 | 判断 |
|---|---|---|
| 人必须读懂 Agent 代码 | 当验证基建足够强，人不需要读 | **短期仍需，长期从"门禁"降级为"排障"** |
| AGENTS.md/PROMPT.md 是 Instructions 层 | 自然语言指令太原始，需要形式化规格 | **方向对，markdown 是当前最实用载体，形式化规格是下一步** |
| 测试是最高 ROI 的背压 | Agent 时代需要更全面的测试 | **完全同意，"够用"标准要大幅提高** |
| LLM-as-judge 是进阶增强 | AI 审 AI 应该是一等 CI 基建 | **同意，从"可选"升级为"标配"** |
| [[wip-limit\|WIP=1]]、[[pass-state-gating]] | 未直接挑战 | **依然成立，不受影响** |
| 代码判断力是两条线之一 | 终局可能被验证体系替代 | **短期仍需，长期定位会变** |
| 工具就用现有的 | [[agent-native-tooling\|工具需要分化]] | **最有远见的挑战，但落地需要时间** |

## Facebook 迁移 Hack 的模式：怎么推行

现有 harness 体系讲"怎么搭"，没讲"怎么推行"。Facebook 迁移 PHP → Hack 提供了变更管理模式：

1. 工程师会抵抗（更严格的约束 = 更不好写）
2. 别提供退出通道
3. CI 管道逐步收紧，让合规成为最小阻力路径
4. 抵抗不是靠说服消失的，是靠环境变化消失的

直接适用于 harness 推行：AGENTS.md 写了没人遵守？加 pre-commit hook。测试没人跑？加 CI gate。Agent 总是跳过验证？改 pass-state gating 规则。**不是靠说服，是靠管道收紧。**

## Harness 的终局

现有 harness 的隐含假设是"人还在循环里"。SkipLabs 指向的终局是 **lights-out**——人不在循环里，信任完全建立在过程上。

这意味着 harness 的最终形态不是"更好的辅助工具"，而是**让人可以不在场的信任基建**：

- **上游**：形式化规格层替代自然语言指令，类型系统约束 Agent 的行为空间
- **验证**：测试覆盖 + AI 审 AI 作为一等 CI，替代人类 code review 作为质量门禁
- **下游**：生产监控 + 快速回滚，替代人类"看一眼觉得没问题"的直觉判断

在这个终局里，人的角色从"审代码"变成"建基建"——从 [[harness-deliberate-practice|训练指南]]第 5 周说的"在循环外观察"，到终极的"根本不在场"。[[subagent-scheduling|Agent 当调度员]]、[[ralph-loop|Ralph 循环]]、[[backpressure-signals|背压信号]]——这些机制不是为了让人更好地介入，而是为了让人的介入变得不必要。

但这个终局不是现在。**现在该做的不是跳过"人还在循环里"的阶段，而是用那个阶段来建好让 lights-out 成为可能的基建。** 每一条你写的测试、每一个你加的 CI gate、每一个你建的形式化合约，都是在把"人必须在场"的必要性降低一点。直到有一天，你发现自己不需要在场了。

---

[[codegen-as-compiler-output]] · [[agent-native-tooling]] · [[harness-defined]] · [[agents-md]] · [[backpressure-signals]] · [[acceptance-driven-backpressure]] · [[pass-state-gating]] · [[ralph-loop]] · [[subagent-scheduling]] · [[harness-deliberate-practice]] · [[wip-limit]] · [[overconfidence-bias]]
