# Process Over Prose

**TL;DR** 给 agent 的工作流，不是参考文档。可执行步骤 + 检查点 + 退出标准，胜过长篇文章。Agent 能执行流程，但只能"读"散文——然后跳过。

## What it means

把一篇 2000 字的测试最佳实践文章放进 agent 上下文里，agent 会读它，生成看起来合理的文本，然后跳过真正的测试。把一个工作流放进去——先写失败的测试，运行它，确认它失败，写最小代码让它通过，确认它通过，再重构——agent 就有事可做，而你也有东西可验证。

**流程优先于散文。工作流优先于参考资料。有退出标准的步骤，优先于没有退出标准的长篇文章。** ([[agent-skills-osmani]])

## 为什么不是"短文档比长文档好"

这个原则和 [[progressive-disclosure]] 有关但不同。Progressive disclosure 说的是"不要一次加载太多"——解决的是信息量问题。Process over prose 说的是"即使信息量相同，工作流也比文章有效"——解决的是信息形态问题。

一个 400 字的工作流和一个 400 字的参考文章，token 数一样，但前者有检查点和退出标准，agent 可以逐步执行并产出证据；后者只有声明，agent 读了就算，没有可验证的产出。

## 对人类同样成立

团队手册 200 页，人在压力下没人会读。如果是一小组带检查点的工作流，人们真的会运行它们。这不仅适用于 agent skills，也适用于 onboarding 指南和 runbooks。

如果你正在写一篇 2000 字的"我们如何处理 X"，那你写的是参考材料。把它转换成带检查点的工作流，文档会缩短到 400 字，而且人们真的会运行。([[agent-skills-osmani]])

## 和 wiki 其他概念的关系

- [[agents-md]] 应该是工作流入口，不是百科全书。每条规则应该告诉 agent "做什么"而不是"知道什么"
- [[progressive-disclosure]] 是 process over prose 的信息量维度；process over prose 是它的形态维度
- [[backpressure-signals]] 是 process over prose 的验证端：工作流的退出标准通常由测试/构建/检查来执行
- [[anti-rationalization]] 是 process over prose 的防御端：文章可以被合理化绕过，工作流的检查点让绕过更难

## 判断标准

问自己：如果 agent 读了这个文档，它的下一步是可验证的动作，还是只是"知道了"然后继续？

- "测试必须先写" → 散文（agent 读完没有具体动作）
- "1. 写失败的测试 2. 运行确认失败 3. 写最小代码 4. 运行确认通过" → 流程（每步有可验证产出）

## See also

- [[agent-skills-osmani]] — 来源
- [[progressive-disclosure]] — 信息量控制
- [[agents-md]] — AGENTS.md 应该是工作流
- [[backpressure-signals]] — 工作流退出标准的执行层
- [[anti-rationalization]] — 工作流比文章更难被合理化绕过
- [[pass-state-gating]] — 工作流完成的结构性保证
