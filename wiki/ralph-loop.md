# The Ralph Loop

**TL;DR** A dumb bash `while` loop that keeps restarting an LLM agent with fresh context. The plan file on disk is the only shared state between iterations. No orchestration, no memory, no sophistication — just `cat PROMPT.md | claude` forever.

## What it means

The Ralph loop is the simplest possible outer loop for autonomous coding: a shell script feeds the same prompt to the agent on every iteration, the agent reads the plan file from disk, picks a task, implements it, commits, and exits. Then the loop restarts with a completely fresh context window.

```bash
while :; do cat PROMPT.md | claude ; done
```

That's it. No session state survives. No complex orchestration. The `IMPLEMENTATION_PLAN.md` file on disk is the only memory between iterations.

## Why this works

Each iteration is deterministic in setup: the same `PROMPT.md` + `AGENTS.md` are loaded every time. The agent reads the current plan state from disk and acts on it. After committing, the updated plan becomes the starting point for the next iteration.

This gives you three properties for free:

1. **Fresh context** — no accumulation of stale information, no [[context-anxiety]]
2. **WIP=1** — one task per iteration, naturally bounded by [[wip-limit]]
3. **Self-healing** — a bad iteration can't corrupt future iterations (the plan file is the only mutable state, and it's text on disk)

## The two modes

The same loop mechanism serves both planning and building:

| Mode | Prompt | What happens |
|---|---|---|
| PLANNING | `PROMPT_plan.md` | Gap analysis (specs vs code), generates/updates plan. No implementation. |
| BUILDING | `PROMPT_build.md` | Reads plan, picks most important task, implements, tests, commits. |

Planning often completes in 1-2 iterations. Building runs for as many tasks as needed.

## The building iteration lifecycle

1. **Orient** — subagents study `specs/*` (requirements)
2. **Read plan** — study `IMPLEMENTATION_PLAN.md`
3. **Select** — pick the most important task
4. **Investigate** — subagents study relevant `/src` ("don't assume not implemented")
5. **Implement** — N subagents for file operations
6. **Validate** — 1 subagent for build/tests (backpressure)
7. **Update plan** — mark task done, note discoveries
8. **Update AGENTS.md** — if operational learnings
9. **Commit**
10. **Loop ends** → context cleared → next iteration starts fresh

## Enhanced versions

The minimal loop can be extended with: mode selection (`plan`/`build` arguments), max-iterations cap, git push after each iteration, and `--output-format=stream-json` for monitoring. These are convenience features — the core mechanism stays the same.

## The deeper pattern

The Ralph loop is an instance of the [[diagnostic-loop]] pattern: each iteration is a discrete experiment, the plan file is the accumulated knowledge, and regeneration is cheap. It embodies [[progressive-disclosure]] (short prompt + separate operational guide), [[pass-state-gating]] (only the plan marks things done), and the principle that [[three-layer-termination|verification must pass]] before commit.

The antidote to a bad plan isn't a smarter agent — it's `rm IMPLEMENTATION_PLAN.md` and one more planning loop.

([[ralph-playbook]])
