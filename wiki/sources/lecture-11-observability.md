---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/
raw: raw/docs/en/lectures/lecture-11-why-observability-belongs-inside-the-harness/index.md
---

# Lecture 11. Observability Belongs Inside the Harness

Without observability, agents make decisions under uncertainty. With it, they converge in one pass.

## What it means

Two types of observability:

- **Runtime observability**: System signals — logs, traces, events. Answers "what did the system do?"
- **Process observability**: Harness decision artifacts — plans, scoring rubrics. Answers "why was this change accepted?"

Both are needed. Runtime tells you what happened; process tells you whether it was the right decision.

## Key concepts

- **Task Trace**: Complete decision-path record, like distributed tracing for agent actions
- **Sprint Contract**: Pre-coding agreement on scope, standards, exclusions
- **Evaluator Rubric**: Structured quality scoring across dimensions (code correctness, architecture compliance, test coverage)

## How to build it

1. **Runtime signal collection**: Harness automatically collects logs, traces, lifecycle events
2. **Sprint contracts**: Before each task, agree on scope, standards, and what's excluded
3. **Evaluator rubrics**: Quantifiable quality dimensions with scoring
4. **OpenTelemetry integration**: Standardize traces with spans for tasks and verification steps

## Case study

Dark mode feature:
- **Without observability**: 3-4 retries, 45 mins, poor quality
- **With observability**: 1 iteration, 15 mins, high quality

## See also

- [[lecture-10-e2e-testing]] — verification as the ground truth
- [[lecture-12-clean-state]] — clean state ensures observability persists
- [[sprint-contract]] — pre-task scope agreement
- [[evaluator-rubric]] — structured quality scoring
- [[task-trace]] — distributed tracing for agents
