---
type: guide
date: 2025-01
author: Clayton Farr
url: https://ClaytonFarr.github.io/ralph-playbook/
raw: raw/how-to-ralph-wiggum/README.md
---

# The Ralph Playbook

**TL;DR** Ralph is a loop-based coding agent pattern (by Geoffrey Huntley) where a dumb bash script keeps restarting Claude with fresh context, and a plan file on disk is the only shared state between iterations. The playbook spells out the three-phase workflow, the key principles, and the exact file/prompt templates.

## What it means

Ralph isn't "a loop that codes." It's a funnel: **Phase 1** defines requirements (human + LLM conversation → specs), **Phase 2** generates a plan (gap analysis against code → `IMPLEMENTATION_PLAN.md`), and **Phase 3** builds from the plan (one task per loop iteration → commit → fresh context). The same loop mechanism serves both planning and building — just swap `PROMPT.md`.

The core insight: **context is everything.** A 200K-token window is really ~176K usable, and you want 40-60% utilization for the "smart zone." One task per loop = 100% smart zone utilization. So the main agent becomes a scheduler, and subagents do the real work (each gets ~156KB garbage-collected).

## The key principles

1. **Context is everything** — tight tasks, one task per loop, subagents as memory extension. Markdown over JSON for token efficiency.
2. **Steering = upstream signals + downstream backpressure** — upstream: deterministic setup (same files loaded every iteration); downstream: tests/typechecks/lints that reject bad work. LLM-as-judge can extend backpressure to subjective criteria.
3. **Let Ralph Ralph** — lean into the LLM's ability to self-identify, self-correct, and self-improve. Eventual consistency through iteration.
4. **Move outside the loop** — your job is to engineer the setup, not sit in the loop. Observe, course-correct, tune reactively. The plan is disposable: if it's wrong, throw it out and regenerate.

## The loop mechanics

Outer loop: `while :; do cat PROMPT.md | claude; done` — dumb bash, no orchestration. The plan file on disk is the shared state. Each iteration reads the plan, picks the most important task, implements, commits, exits. Fresh context next iteration.

Inner loop: single task, no hard limit. Scope discipline ("one task"), backpressure (tests must pass), and natural completion (agent exits after commit) keep it bounded.

Enhanced versions add mode selection (plan/build), max-iterations, and git push after each iteration. [[ralph-loop]]

## The file structure

| File | Purpose |
|---|---|
| `loop.sh` | Outer loop script |
| `PROMPT_plan.md` | Planning mode instructions |
| `PROMPT_build.md` | Building mode instructions |
| `AGENTS.md` | Operational "how to build/run" guide (~60 lines, NOT a changelog) |
| `IMPLEMENTATION_PLAN.md` | Prioritized task list (generated/updated by Ralph) |
| `specs/*.md` | One per JTBD topic of concern |

Key language patterns from Geoff: "study" (not "read"), "don't assume not implemented," "using parallel subagents," "Ultrathink," "capture the why," "keep it up to date."

## The security model

`--dangerously-skip-permissions` is required for autonomy. The sandbox becomes your only security boundary. Philosophy: "It's not if it gets popped, it's when. And what is the blast radius?" Options: Docker (local), E2B/Sprites/Modal/Cloudflare (remote). [[sandbox-for-agents]]

## Proposed enhancements

- **AskUserQuestion for Planning** — use Claude's built-in interview tool during Phase 1 to clarify JTBDs and acceptance criteria before writing specs.
- **Acceptance-Driven Backpressure** — derive test requirements from acceptance criteria during planning, preventing "cheating" (claiming done without tests). [[acceptance-driven-backpressure]]
- **Non-Deterministic Backpressure** — LLM-as-judge for subjective criteria (tone, aesthetics, UX). Binary pass/fail, converges through iteration. [[backpressure-signals]]
- **Ralph-Friendly Work Branches** — scope at plan creation (deterministic), not task selection (probabilistic). One scoped `IMPLEMENTATION_PLAN.md` per branch.
- **JTBD → Story Map → SLC Release** — reframe topics of concern as activities (verbs), sequence into user journey, slice into Simple/Lovable/Complete releases. [[story-map-slc]]

## Why it matters for harness engineering

Ralph is a concrete implementation of several harness principles: [[wip-limit|WIP=1]] (one task per loop), [[pass-state-gating]] (only the plan file marks tasks done), [[three-layer-termination]] (tests must pass before commit), and [[progressive-disclosure]] (short AGENTS.md, not a 600-line manual). The loop itself is the harness — the agent is just the engine.
