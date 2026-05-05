# WIP Limit

Work-in-progress limit. The Kanban principle applied to AI agents. WIP=1 is the safest default.

## What it means

An agent with no WIP limit will start 5 features and finish 0. The prompt "implement the backend" with no boundaries leads to overreach. WIP=1 means: finish one feature completely (including verification) before starting the next. ([[lecture-07-task-boundaries]])

## The evidence

- **WIP=5 (unconstrained)**: 800 lines, 12 files, 20% e2e pass rate, 3/8 features complete
- **WIP=1**: 1200 lines, 4 files per feature, 100% e2e pass rate, 7/8 features complete

More code doesn't mean more done. Focused completion beats scattered activity. ([[lecture-07-task-boundaries]])

## How to enforce

Put the WIP limit in CLAUDE.md as an explicit rule. The [[feature-list]] tracks state — if any feature is "active," no new feature can be started until it reaches "passing."

## Verified Completion Rate

VCR = features passing e2e / features started. Block new tasks if VCR < 1.0. ([[lecture-07-task-boundaries]])

## See also

- [[feature-list]] — the data structure that tracks WIP
- [[scope-surface]] — the DAG of task states
- [[ralph-loop]] — WIP=1 enforced naturally: one task per loop iteration
- [[story-map-slc]] — WIP=1 at the release level: one SLC slice at a time
- [[agent-skills-osmani]] — Osmani's "scope discipline": only touch what you were asked to touch
- [[anti-rationalization]] — pre-empting excuses for scope creep
- [[lecture-07-task-boundaries]] — the full argument
- [[lecture-09-premature-victory]] — why "done" isn't done until verification passes
