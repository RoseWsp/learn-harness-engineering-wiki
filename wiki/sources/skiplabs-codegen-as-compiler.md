---
type: article
date: 2026-03-09
author: Hugo Venturini (SkipLabs)
url: https://skiplabs.io/blog/codegen_as_compiler
raw: n/a
---

# Treat Agent Output Like Compiler Output

**TL;DR** 没人审查编译器输出的汇编——不是因为盲目信任，而是因为建了一整套体系让审查变得不必要。对 Agent 产出，这套体系还不存在。问题不是"该不该信任 Agent"，而是"有没有建好让信任变得合理的基建"。

## 核心论点

Philip Su 提出"免审查代码库（lights-out codebases）"，Venturini 推进一步：lights-out 让人害怕的真正原因不是不理性，而是**支撑信任的上游和下游 apparatus 几乎不存在**。

编译器产出不需要人审，因为：
- **上游**：类型系统、形式化合约约束代码在运行前能做什么
- **验证层**：编译器是确定性的——同样源码永远产出同样二进制
- **下游**：测试、fuzzing、sanitizer、生产监控、回滚

我们信任的是**过程**，不是**制品**。对 Agent 产出，这三层都没有建好。

## 对现有 harness 的关键判断

1. **测试需要比人类时代更全面**——Agent 是不确定性的，能以 50 倍速率生成"看起来对但实际有微妙错误"的代码
2. **AI 审 AI 应该是一等 CI 基建**，不是可选的增强
3. **硬件芯片公司的模式是先例**——黑盒组件 + 验收测试，不需要人审内部实现。但芯片验证本身是一个**学科**，有工具、有形式化方法、有专职团队设计测试 harness。软件还没有这个传统

## 引用

> The question isn't "should we trust agent output?" It's "have we built the infrastructure that makes that trust reasonable?"

> The scary part isn't the lights-out codebase. The scary part is how few teams are treating what replaces the review as serious engineering work.
