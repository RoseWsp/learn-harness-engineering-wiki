---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-07-why-agents-overreach-and-under-finish/
raw: raw/docs/en/lectures/lecture-07-why-agents-overreach-and-under-finish/index.md
---

# Lecture 07. Draw Clear Task Boundaries

Agents that "do a little extra" end up finishing nothing. WIP=1 is the safest default.

## What it means

Two failure modes: **overreach** (starting too many tasks at once) and **under-finish** (none of them pass end-to-end verification). A prompt that says "implement the backend" with no boundaries leads to 5 features started, 0 passing.

## Key concepts

- **WIP Limit**: Kanban principle applied to agents — limit active tasks. WIP=1 is safest.
- **Completion Evidence**: Not "code looks fine" but executable verification that passes.
- **Scope Surface**: A DAG tracking task states (not_started → active → blocked → passing).
- **Verified Completion Rate (VCR)**: Ratio of tasks passing e2e verification. Block new tasks if VCR < 1.0.

## How to fix it

1. **Enforce WIP=1**: Explicit rule in CLAUDE.md — work on one feature at a time
2. **Define completion evidence**: Every task needs an executable verification command
3. **Externalize scope surface**: Use a machine-readable file (JSON/Markdown) to track task states
4. **Monitor VCR**: Block new tasks if current ones aren't verified passing

## Case study

- **Unconstrained (WIP=5)**: 800 lines, 12 files, 20% e2e pass rate, 3/8 features complete in 3 sessions
- **WIP=1**: 1200 lines, 4 files per feature, 100% e2e pass rate, 7/8 features complete in 4 sessions

## See also

- [[lecture-08-feature-lists]] — feature lists as the data structure for scope
- [[lecture-09-premature-victory]] — why agents say "done" too early
- [[wip-limit]] — the Kanban principle for agents
- [[scope-surface]] — tracking task states
- [[harness-defined]] — the five subsystems
