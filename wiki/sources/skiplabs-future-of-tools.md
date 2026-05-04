---
type: article
date: 2026-03-23
author: Hugo Venturini (SkipLabs)
url: https://skiplabs.io/blog/future_of_tools_for_ai
raw: n/a
---

# Code Was Never for Machines — Until Now

**TL;DR** 编程语言发展的整条历史就是让人更容易读。但 Agent 不需要可读性——它需要冗长精确的输出、严格吹毛求疵的执行、机器可解析的结构化信息。工具将分化为"给人用的"和"给 Agent 用的"，后者更严格、更形式化、更不好写，但对 Agent 更好。

## 核心论点

编程语言的演进：汇编 → C → Python/Ruby，每一步都是在优化人类可读性。Python 的缩进规则不是技术必需，是可读性约定。所有工具（错误信息、CLI 输出、文档格式）都在优化人类阅读者。直到现在，代码的消费者一直是人。

Agent 反转了这个假设：
- Agent 受益于**冗长**——长、精确、无歧义的工具输出比短、巧妙、人类优化的更容易解析
- Agent 受益于**吹毛求疵的执行**——出错时大声且具体地失败，而不是静默类型强转或吞掉错误
- Agent 受益于**强类型系统**——不是因为需要护栏，而是因为类型是描述"代码应该做什么"的信息最密集的方式

## Facebook 迁移 PHP → Hack 的案例

Julien Verlaguet 在 Facebook 建 Hack 替代 PHP：更冗长、更精确、更不好写。工程师疯狂抵抗——要退出通道、要豁免、要延期。组织守住底线：CI 管道逐步收紧，更多检查、更严 gate、更少容忍无类型代码。抵抗不是靠说服消失的，是靠环境变化消失的。

同样的迁移会发生：工具分化成给人用的和给 Agent 用的，后者更严格、更形式化，人会抵抗，但系统级论证压倒一切。

## SkipLabs 的实践

SKJS（TypeScript 兼容类型检查器）：sound 在标准 TypeScript 不 sound 的地方。对人类更难用，对 Agent 更好用。反应式运行时强制显式依赖合约——手写代码时觉得过度工程，Agent 需要推理"什么依赖什么"时刚刚好。

## 引用

> Pedantry that felt like friction when humans were the authors becomes an asset when the author is an agent operating at scale.

> We made the tools more readable to get more developers. We'll make them less readable — more precise, more formal, more machine-native — to get better agents.
