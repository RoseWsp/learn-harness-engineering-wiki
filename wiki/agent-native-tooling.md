# Agent-Native Tooling

**TL;DR** 编程语言和工具的整条演进历史都在优化人类可读性。Agent 反转了这个假设——它需要的不是可读性，而是精确性、形式化和机器可解析性。工具将分化为"给人用的"和"给 Agent 用的"，后者更严格、更不好写，但对 Agent 更好。

## 编程语言的可读性时代

汇编 → C → Python/Ruby，每一步都在优化人类阅读者。Python 的缩进规则不是技术必需，是可读性约定。Ruby 的语法刻意接近自然语言。TIOBE 指数衡量的是"工程师想写想读什么"，几十年来那就是同一件事。

所有工具同理：错误信息写给人类看，CLI 输出格式化给终端阅读，类型系统可选用以减少人类作者的摩擦。

## Agent 需要的反面

| 人类优化 | Agent 优化 |
|---|---|
| 简洁友好的错误信息 | 完整、结构化、机器可解析的错误输出 |
| 宽容的类型语义（静默强转、吞掉错误） | 吹毛求疵的执行——出错时大声且具体地失败 |
| 短小精悍的 API 输出 | 冗长精确的输出，无歧义 |
| 可读性优先的语法 | 信息密度优先——类型是描述"代码该做什么"的最密集方式 |
| "开发者体验" | "Agent 体验" |

这不是给 Agent 加护栏——是因为 Agent 在不同的约束下工作。冗长是资产，严格是资产，pedantry 是资产。

## Facebook 迁移 PHP → Hack 的启示

Julien Verlaguet 在 Facebook 建 Hack 替代 PHP——更冗长、更精确、更不好写。工程师疯狂抵抗：要退出通道、要豁免、要延期。组织守住底线：CI 管道逐步收紧，合规成为最小阻力路径。抵抗不是靠说服消失的，是靠环境变化消失的。

**对 harness 推行的直接适用**：AGENTS.md 写了没人遵守？加 pre-commit hook。测试没人跑？加 CI gate。Agent 总跳过验证？改 [[pass-state-gating]] 规则。不是靠说服，是靠管道收紧。

## 工具分化

未来会出现 bifurcation：一边继续优化人类作者，另一边针对 Agent 作为主要消费者设计——严格、冗长、形式化、敌视歧义。SkipLabs 的 SKJS 就是实例：在标准 TypeScript 不 sound 的地方做到 sound，对人类更难用，对 Agent 更好用。

但分化不意味着碎片化。Osmani 的 Agent Skills 项目展示了一条中间路径：同一个 `SKILL.md` 文件（markdown + frontmatter）可以在 Claude Code、Cursor rules、Gemini CLI、Codex、Aider、任何接受 system prompt 的 harness 中运行。工作流写一次，运行时负责执行。这是 markdown-with-frontmatter 格式相对于定制化 prompt engineering 的优势——它不绑定任何特定工具，而是利用所有工具共有的 system prompt 接口。([[agent-skills-osmani]])

这个可移植性对 harness 体系有实际意义：你不需要为每个工具写一套规则，而是写一套工作流，让工具各自适配。这和 [[progressive-disclosure|渐进式披露]] 的路由思路一致——载体标准化，内容按需加载。

## 对 harness 体系的意义

现有 [[agents-md|Instructions 层]] 的 markdown 文件是"人类可读时代"的产物。走向 [[agent-native-tooling|Agent 原生工具]] 意味着：
- 错误信息、CLI 输出、测试报告应该有结构化的机器可解析格式
- 类型系统应该更严格而非更宽容——Agent 不需要"开发者体验"，它需要信息密度
- [[progressive-disclosure|渐进式披露]] 的载体可能从 markdown 文件演变为某种形式化合约

这不是推翻 harness，而是说 **harness 的载体本身可能需要从"人可读"走向"Agent 可执行"**。

([[skiplabs-future-of-tools]])
