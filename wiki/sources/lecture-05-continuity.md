---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/
raw: raw/docs/en/lectures/lecture-05-why-long-running-tasks-lose-continuity/index.md
---

# Lecture 05. Long-Running Tasks Lose Continuity

Agents lose context across sessions like amnesiac craftsmen. Structured state persistence is the cure.

## What it means

Context windows are finite. Long tasks exhaust them. Intermediate reasoning is lost — only code remains. When context runs low, agents experience "context anxiety" and rush to premature convergence.

Different models handle this differently: Sonnet 4.5 shows severe anxiety (needs context reset), while Opus 4.5 shows mild anxiety (compaction works).

## Continuity artifacts

Three artifacts that preserve state across sessions:

1. **PROGRESS.md** (core journal): current state, last commit, test status, completed/in-progress work, known issues, next steps
2. **DECISIONS.md** (decision memos): why option B over A, library choices, optimizations skipped
3. **Git commits as checkpoints**: every meaningful state change gets committed

## The init.sh protocol

- **Session start**: Read PROGRESS + DECISIONS → run health checks → orient
- **Session end**: Update files → commit → leave clean state

Think of it as clock-in / clock-out for agents.

## Key metrics

- **Rebuild Cost**: Time to reach executable state in a new session. Target: <3 minutes.
- **Mixed strategy**: Short tasks can stay in-session; long tasks need external artifacts.

## Case study

Blog system with 12 features:
- Without journal: 7/12 features, 3 defects, 15 min rebuild per session
- With journal: 12/12 features, 1 defect, 3 min rebuild per session

## See also

- [[lecture-06-initialization-phase]] — the dedicated initialization phase
- [[lecture-03-repo-as-system-of-record]] — repo as source of truth
- [[lecture-12-clean-state]] — clean handoff at session end
- [[progress-md]] — the core journal artifact
- [[context-anxiety]] — why agents rush when context is low
