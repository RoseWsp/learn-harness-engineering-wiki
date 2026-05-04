---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/
raw: raw/docs/en/lectures/lecture-06-why-initialization-needs-its-own-phase/index.md
---

# Lecture 06. Initialization Needs Its Own Phase

Don't mix setup and implementation. Pour the foundation before building the walls.

## What it means

When agents jump straight to coding without initialization, they build on shaky ground. Missing dependencies, untested toolchains, and implicit assumptions create landmines that explode in later sessions.

## The problem with mixing

- Agent rushes to code → bad foundation
- Unverified accumulation — code without tests, piling up
- Wasted budget on re-discovery (re-figuring out what was already known)
- Implicit assumption landmines — subsequent sessions contradict choices

## Initialization output

Five deliverables that must exist before any feature work:

1. **Runnable environment** — the foundation is poured, `npm install` works
2. **Verifiable test framework** — at least 1 passing test
3. **Bootstrap contract document** — how to run, test, see progress
4. **Task breakdown** — ordered list with acceptance criteria
5. **Git checkpoint** — clean commit point

## The bootstrap contract

Four conditions a new session must satisfy:

- Can start the project from scratch
- Can run tests
- Can see current progress
- Can pick up next steps

## Warm start strategy

Use project templates (create-react-app, fastapi-template) to preset infrastructure. Don't reinvent scaffolding.

## Key metrics

- **Time to First Verification**: How fast can you confirm the environment works?
- **Downstream Usability**: % of sessions that execute without implicit knowledge

## Case study

- Mixed approach: 60% more rebuild time, inefficient sessions
- Dedicated initialization: 3 min rebuild per session, faster overall

## See also

- [[lecture-05-continuity]] — state persistence across sessions
- [[lecture-12-clean-state]] — clean handoff at session end
- [[bootstrap-contract]] — the four conditions for starting work
- [[init-sh]] — the initialization script
