# AGENTS.md

This repo is optimized for long-running coding-agent work. Keep this file short —
it is a routing layer into the system-of-record docs, not a giant instruction dump.

## Startup Workflow

Before changing code:

1. Confirm repo root with `pwd`.
2. Read `PROGRESS.md` for current state and last session's work.
3. Read `IMPLEMENTATION_PLAN.md` for the task queue.
4. Read `feature-list.json` for feature states.
5. Run `bash init.sh` to verify bootstrap contract.
6. If baseline verification is failing, repair baseline before adding scope.

## Build & Run

<!-- FILL IN: your project's build/run commands -->
```
# Install
npm install

# Dev
npm run dev

# Build
npm run build
```

## Validation

Run these after every change to get immediate feedback:

<!-- FILL IN: your project's verification commands -->
```
# Tests
npm test

# Type check
npm run typecheck

# Lint
npm run lint
```

## Routing Map

- `IMPLEMENTATION_PLAN.md` — prioritized task queue, current iteration
- `feature-list.json` — machine-readable feature states and verification
- `PROGRESS.md` — session journal, clock-in/clock-out record
- `docs/testing-standards.md` — test writing rules
- `docs/api-patterns.md` — API design guidelines
- `docs/quality-document.md` — module quality scores (A-F)

## Working Contract

- **WIP=1**: Only one active feature at a time. No exceptions.
- **Pass-state gating**: You cannot mark features as "passing" — only the harness (tests) can.
- **Tests before code**: Write failing tests first, then implement.
- **Three-layer termination**: Syntax → unit tests → e2e. All three must pass before commit.
- **Clean state only**: Commit only when all five clean-state conditions are met (see `docs/clean-state-checklist.md`).
- If you change behavior, update docs in the same session.
- If you see repeated review feedback, promote it into a mechanical rule or linter.

## Anti-Rationalization Table

| Excuse | Rebuttal |
|---|---|
| "Too simple for a spec" | Acceptance criteria still apply. 5 lines minimum. |
| "Write tests later" | "Later" never comes. Write failing tests first. |
| "Tests passed, ship it" | Passing is evidence, not proof. Did you check runtime? |
| "Just a quick fix" | Quick fixes skip verification. Run all three layers. |
| "I'll update docs later" | Docs rot in 10 minutes. Update in the same session. |
| "Existing code is messy" | Clean it in a separate task. Don't scope-creep. |

## Definition Of Done

A change is done only when ALL of the following are true:

1. Target behavior is implemented
2. Required verification actually ran and passed
3. Evidence is recorded in `feature-list.json`
4. Affected docs remain current
5. The repo can restart cleanly from `bash init.sh`

## End Of Session

Before ending a session:

1. Update `PROGRESS.md` with what was done and what's next.
2. Update `feature-list.json` states.
3. Update `IMPLEMENTATION_PLAN.md` — mark completed, add findings.
4. Record new debt in `IMPLEMENTATION_PLAN.md` if you deferred anything.
5. Leave the repo in a restartable state with a clear next action.
