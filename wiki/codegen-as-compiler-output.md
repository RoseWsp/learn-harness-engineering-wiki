# Codegen as Compiler Output

**TL;DR** 没人审查编译器生成的汇编——不是因为信任编译器，而是因为建了一整套验证体系让审查变得不必要。对 Agent 产出也应如此：问题不是"该不该信任 Agent"，而是"有没有建好让信任变得合理的基建"。

## 编译器类比

编译器产出不需要人审，因为三层 apparatus 把信任从"制品"转移到了"过程"：

| 层 | 编译器时代 | Agent 时代 |
|---|---|---|
| 上游 | 类型系统、形式化合约 | Prompts——原始的、非形式化的 |
| 验证 | 编译器是确定性的，同源码同产出 | Agent 不确定，能 50 倍速率生成 plausible-but-wrong 代码 |
| 下游 | 测试、fuzzing、sanitizer、生产监控 | 测试存在但不全面，AI 审 AI 是可选增强而非标配 |

Agent 时代每层都比编译器时代弱。这不是反对 lights-out 的论据——而是"负责任地走向 lights-out 到底需要什么"的清点。

## 硬件芯片的先例

芯片公司用黑盒组件 + 验收测试，不需要人审内部实现。但注意：芯片验证本身是一个**学科**，有形式化方法、有专职团队、有工具链。软件的正式规格文化远比硬件弱，所以软件做这件事可能**更难**。

## 对 harness 体系的意义

现有 [[harness-defined|harness]] 的 Feedback 层（测试做背压）是最接近编译器验证层的部分，但标准远远不够——Agent 作者犯错的方式比人类更微妙，需要"实质性更全面"的测试覆盖。[[backpressure-signals|AI 审 AI]] 应该从"可选增强"升级为一等 CI 基建。

上游的 [[agents-md|Instructions 层]]（AGENTS.md、PROMPT.md）本质上还是自然语言指令，类比编译器时代则是"还没有类型系统"。走向 [[codegen-as-compiler-output|形式化规格]] 是必然方向，但当前 markdown 是最实用的载体。

([[skiplabs-codegen-as-compiler]])
