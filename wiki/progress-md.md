# PROGRESS.md

The core journal artifact. The agent's clock-in/clock-out record for every session.

## What it contains

- Current state: what's done, what's in progress
- Last commit: the git checkpoint
- Test status: are we green?
- Completed work: features that passed verification
- In-progress work: what's active now
- Known issues: bugs, blockers, technical debt
- Next steps: what the next session should pick up

## Why it matters

Without PROGRESS.md, every session starts from scratch. The agent re-discovers what was done, re-reads code, re-builds context. **Rebuild cost** — the time to reach an executable state — should be <3 minutes. Without a progress journal, it's typically 15+ minutes. ([[lecture-05-continuity]])

## The init.sh protocol

- **Session start**: Agent reads PROGRESS.md + DECISIONS.md → runs health checks → orients
- **Session end**: Agent updates PROGRESS.md → commits → leaves [[clean-state-checklist|clean state]]

Think of it as clock-in / clock-out for agents. ([[lecture-06-initialization-phase]])

## Case study

Blog system with 12 features:
- Without journal: 7/12 features, 3 defects, 15 min rebuild
- With journal: 12/12 features, 1 defect, 3 min rebuild ([[lecture-05-continuity]])

## See also

- [[lecture-05-continuity]] — the full argument
- [[cold-start-test]] — question 4: what's the current state?
- [[feature-list]] — the structured version of progress tracking
- [[lecture-12-clean-state]] — clean state at session end
