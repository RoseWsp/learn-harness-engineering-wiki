---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-01-why-capable-agents-still-fail/
raw: raw/docs/en/lectures/lecture-01-why-capable-agents-still-fail/index.md
---

# Lecture 01. Strong Models Don't Mean Reliable Execution

Same model, same prompt, wildly different results — the harness makes the difference.

## What it means

Benchmark scores don't predict real-world agent performance. Anthropic ran a controlled experiment: Opus 4.5 with no harness produced a broken game in 20 minutes ($9); with a full harness it built a playable one in 6 hours ($200). OpenAI reported the same — Codex in a well-harnessed repo goes from "unreliable" to "reliable," a qualitative shift, not incremental.

## Where agents actually get stuck

Six failure patterns, all harness-induced:

1. **Underspecified tasks** — "add search" means nothing. The agent guesses, and wrong guesses cost more than being specific.
2. **Implicit conventions** — SQLAlchemy 2.0 syntax, OAuth rules, folder structure — if it's only in your head or Slack, it doesn't exist for the agent.
3. **Broken environments** — wrong Node version, missing deps, stale migrations. The agent inherits your mess.
4. **No verification** — agent says "done" but nothing passes. No tests, no lint, no smoke check.
5. **Context anxiety** — approaching context limits, the agent rushes and declares premature completion.
6. **Lost continuity** — every new session starts from scratch. No memory of past decisions, no progress file.

## The diagnostic loop

Don't blame the model. Attribute failures to one of five layers: task spec, context, environment, verification, state. Fix the layer, re-execute, measure.

## Key terms

- **Capability Gap**: Benchmark performance vs real-world performance
- **Harness**: Everything outside model weights — instructions, tools, environment, state, feedback
- **Harness-Induced Failure**: Model is capable but environment is defective
- **Verification Gap**: Agent's confidence vs actual correctness
- **Definition of Done**: Machine-verifiable completion criteria

## Key evidence

- Anthropic experiment: bare (20min, $9, broken) vs harness (6hrs, $200, playable) — same Opus 4.5
- OpenAI: 1M LOC internal product built by agents with Codex + harness
- Team report: Claude Sonnet with AGENTS.md → 60% better context efficiency

## What to do

Write a [[definition-of-done]]. Create [[agents-md]]. Build a [[diagnostic-loop]]. Quantify improvements.

## See also

- [[lecture-02-what-harness-is]] — the five subsystems that make up a harness
- [[lecture-09-premature-victory]] — why agents say "done" too early
- [[harness-defined]] — what "harness" actually means
- [[capability-gap]] — why benchmarks mislead
