# Clean State Checklist

Five conditions that must hold when a session ends. Non-negotiable.

## The five conditions

1. **Build passes** — `npm run build` succeeds
2. **Tests pass** — `npm run test` is green
3. **Progress is recorded** — PROGRESS.md is updated
4. **No stale artifacts** — no temporary files, debug code, or commented-out blocks
5. **Startup path is available** — next session can reach executable state without human help

If you can't get all five, roll back to the last known good state. Half-states are worse than rolling back. ([[lecture-12-clean-state]])

## Session integrity

Either fully commit a clean state or revert. No "I'll fix it tomorrow." Tomorrow's session inherits your mess and spends 30-60 minutes diagnosing it. ([[lecture-12-clean-state]])

## The evidence

12-week Electron app development:
- **Without cleanup**: Week 12 — 68% build pass, 61% test pass, 60+ min startup
- **With cleanup**: Week 12 — 97% build pass, 95% test pass, 9 min startup

Clean state is a 7x improvement in startup time. ([[lecture-12-clean-state]])

## See also

- [[lecture-12-clean-state]] — the full argument
- [[lecture-05-continuity]] — state persistence across sessions
- [[progress-md]] — recording progress as condition 3
- [[harness-rot]] — what happens when cleanup is neglected
