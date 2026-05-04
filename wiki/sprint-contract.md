# Sprint Contract

A pre-coding agreement on scope, standards, and exclusions. Sets expectations before the agent starts.

## What it contains

- **Scope**: What this task covers and what it explicitly doesn't
- **Standards**: Quality criteria and [[evaluator-rubric|rubrics]] that define "done"
- **Exclusions**: What the agent should not touch, even if it seems related

## Why it matters

Without a sprint contract, scope creep is inevitable. The agent starts on one feature, notices an adjacent issue, and "does a little extra." This is overreach — the same problem [[wip-limit]] addresses, but at the task level rather than the feature level. ([[lecture-11-observability]])

## Relationship to observability

Sprint contracts are part of **process observability** — they answer "why was this change accepted?" Combined with runtime signals (logs, traces), they give a complete picture of agent decision-making. ([[lecture-11-observability]])

## See also

- [[evaluator-rubric]] — the quality scoring that sprint contracts reference
- [[wip-limit]] — constraining scope at the feature level
- [[lecture-11-observability]] — the full argument on observability
- [[scope-surface]] — tracking what's in and out of scope
