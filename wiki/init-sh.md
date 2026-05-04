# init.sh

The initialization script. The agent's clock-in/clock-out mechanism.

## What it does

- **Session start**: Read PROGRESS.md + DECISIONS.md → run health checks → orient → begin work
- **Session end**: Update progress files → commit → leave [[clean-state-checklist|clean state]]

Think of it as the formal handoff protocol between sessions. The next agent runs init.sh and immediately knows the state of the project. ([[lecture-05-continuity]], [[lecture-06-initialization-phase]])

## Why it matters

Without a formal initialization protocol, each session spends 15+ minutes re-discovering project state. With init.sh, rebuild cost drops to <3 minutes. ([[lecture-05-continuity]])

## See also

- [[lecture-06-initialization-phase]] — initialization as a dedicated phase
- [[progress-md]] — the journal that init.sh reads/writes
- [[bootstrap-contract]] — what init.sh ensures
