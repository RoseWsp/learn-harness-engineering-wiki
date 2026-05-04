# Index

## Sources

- [[lecture-01-capable-agents-still-fail]] — Strong models don't mean reliable execution; the harness makes the difference
- [[lecture-02-what-harness-actually-is]] — A harness is five subsystems, not a prompt file
- [[lecture-03-repo-as-system-of-record]] — Knowledge not in the repo doesn't exist for agents
- [[lecture-04-giant-instruction-file-fails]] — 600-line AGENTS.md is worse than a 60-line one
- [[lecture-05-continuity]] — Long-running tasks lose continuity without structured state
- [[lecture-06-initialization-phase]] — Initialization needs its own phase, not mixed with implementation
- [[lecture-07-task-boundaries]] — WIP=1 prevents overreach and under-finish
- [[lecture-08-feature-lists]] — Feature lists are foundational harness primitives
- [[lecture-09-premature-victory]] — Agents declare victory too early; use three-layer verification
- [[lecture-10-e2e-testing]] — Only end-to-end testing catches component boundary defects
- [[lecture-11-observability]] — Runtime and process observability reduce retries
- [[lecture-12-clean-state]] — Every session must leave a clean state
- [[ralph-playbook]] — The Ralph pattern: loop-based autonomous coding with plan files and backpressure

## Core Concepts

- [[harness-defined]] — Everything outside model weights; five cooperating subsystems
- [[capability-gap]] — Benchmark performance doesn't predict real-world performance
- [[agents-md]] — The landing page for agents; a routing file, not a manual
- [[feature-list]] — The foundational data structure for scope control
- [[progressive-disclosure]] — Overview first, details on demand
- [[wip-limit]] — Work-in-progress limit; WIP=1 is the safest default
- [[pass-state-gating]] — Only the harness marks features as "passing"
- [[three-layer-termination]] — Syntax → tests → e2e; all three must pass
- [[diagnostic-loop]] — Attribute failures to layers, fix, measure

## Agent Failures

- [[context-anxiety]] — Agents rush when context windows run low
- [[overconfidence-bias]] — Models systematically overestimate accuracy
- [[lost-in-middle-effect]] — Content in the middle of long contexts is 30-40% less effective
- [[harness-rot]] — Harnesses degrade without regular audits

## State & Continuity

- [[progress-md]] — The core journal artifact for session handoff
- [[cold-start-test]] — Five questions a fresh session must answer
- [[clean-state-checklist]] — Five conditions at session end
- [[bootstrap-contract]] — Four conditions before feature work begins
- [[init-sh]] — The clock-in/clock-out script for agents
- [[scope-surface]] — A DAG of task states
- [[quality-document]] — Module quality scores (A-F)

## Verification & Observability

- [[e2e-vs-unit-testing]] — Unit tests miss component boundary defects
- [[backpressure-signals]] — Downstream steering: tests, lints, and LLM-as-judge
- [[acceptance-driven-backpressure]] — Derive test requirements from acceptance criteria before implementation
- [[sprint-contract]] — Pre-coding agreement on scope, standards, exclusions
- [[evaluator-rubric]] — Structured quality scoring framework

## The Ralph Pattern

- [[ralph-loop]] — A dumb bash loop that restarts the agent with fresh context; plan file is shared state
- [[subagent-scheduling]] — Main context as scheduler, subagents as memory extension
- [[sandbox-for-agents]] — Security boundary for autonomous agents; E2B, Sprites, Docker
- [[story-map-slc]] — User journey mapping for Simple/Lovable/Complete releases
