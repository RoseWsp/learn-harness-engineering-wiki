---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/
raw: raw/docs/en/lectures/lecture-12-why-every-session-must-leave-a-clean-state/index.md
---

# Lecture 12. Every Session Must Leave a Clean State

A session that ends with broken builds and red tests costs 30-60 minutes of diagnostic time in the next one.

## What it means

Clean state is a completion requirement, not a nice-to-have. Five conditions must hold when a session ends:

1. Build passes
2. Tests pass
3. Progress is recorded
4. No stale artifacts
5. Startup path is available for the next session

## Session integrity

Either fully commit a clean state or roll back. No half-states. If you can't get to green, revert to the last known good state.

## Key concepts

- **Quality Document**: Active artifact tracking module quality scores (A-F grading)
- **Cleanup Loop**: Immediate (per-session) + periodic (weekly) cleanup
- **Idempotent Cleanup**: Scripts that produce consistent results when run repeatedly

## Dual-mode cleanup

- **Immediate (per-session)**: Run at every session end — verify build, tests, record progress
- **Periodic (weekly)**: Deeper cleanup — remove dead code, update stale docs, simplify harness

## Harness simplification

As models improve, remove outdated constraints. A harness that was necessary for GPT-3.5 may be over-constraining for Opus 4.5. Audit and simplify regularly.

## Case study

12-week Electron app development:
- **Without cleanup**: Week 12 — 68% build pass, 61% test pass, 60+ min startup
- **With cleanup**: Week 12 — 97% build pass, 95% test pass, 9 min startup

## See also

- [[lecture-05-continuity]] — state persistence across sessions
- [[lecture-06-initialization-phase]] — the dedicated initialization phase
- [[clean-state-checklist]] — the five conditions
- [[quality-document]] — module quality scores
- [[harness-rot]] — why harnesses degrade without maintenance
