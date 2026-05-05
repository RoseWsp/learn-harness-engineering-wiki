# AGENTS.md

The landing page for AI agents in your repository. A routing file, not a manual.

## What it is

AGENTS.md is the first thing an agent reads when it enters your project. It answers the Cold-Start questions: what does this project do, how do I run it, how do I test it, what's the current state, where do I find X? ([[lecture-03-repo-as-system-of-record]])

## How to write it

**50-200 lines.** Overview, quick start, hard constraints, topic links. That's it.

The most common mistake is making AGENTS.md too long. A 600-line file is worse than a 60-line one because of the **Lost in the Middle Effect** — content in the middle of a long context is 30-40% less effective. Rules buried in line 400 are essentially ignored. ([[lecture-04-giant-instruction-file-fails]])

## The routing pattern

```
AGENTS.md (80 lines)
├── Project overview (10 lines)
├── Quick start (10 lines)
├── Hard constraints (20 lines)
└── Topic links (40 lines)
    → api-patterns.md
    → database-rules.md
    → testing-standards.md
```

The agent reads the routing file, then follows links to only the relevant topic docs. This is [[progressive-disclosure]]: overview first, details on demand.

## The five non-negotiable principles

Osmani distills five principles that should go into any AGENTS.md, regardless of project: ([[agent-skills-osmani]])

1. **Surface assumptions before building.** Silently held wrong assumptions are the most common failure mode. If the agent doesn't know a constraint, it can't respect it.
2. **Stop and ask when requirements conflict.** Don't guess. A 30-second clarification beats a 30-minute rework.
3. **Push back when necessary.** An agent, like an engineer, is not a yes-machine. If a request would compromise quality, the agent should say so.
4. **Prefer simple, obvious solutions.** Clever tricks are expensive — in maintenance, in debugging, in reviewer time.
5. **Only touch what you were asked to touch.** Scope discipline is the single biggest factor in whether an agent's PR gets merged or reverted.

Principles 1 and 2 are about *information quality* — they address the same problem as the [[cold-start-test]] (does the agent know what it needs to know?). Principle 3 is novel: most harnesses assume the agent should comply, but a senior engineer pushes back on bad requirements. Principle 5 is [[wip-limit]] at the PR level. Principle 4 is the antidote to agent overengineering.

## Each rule should have

- **Source**: Why this rule exists
- **Applicability**: When it applies
- **Expiry condition**: When it can be removed

This prevents [[harness-rot]] — rules that outlive their usefulness.

## Case study

600-line monolithic AGENTS.md → 80-line routing + 3 topic docs → success rate 45% → 72%, security compliance 60% → 95%. ([[lecture-04-giant-instruction-file-fails]])

## Ralph's AGENTS.md

In the [[ralph-loop]] pattern, AGENTS.md has a specific role: it's the "heart of the loop" — a concise, operational "how to build/run" guide loaded every iteration. It must stay brief (~60 lines). Status, progress, and planning belong in `IMPLEMENTATION_PLAN.md`, not here.

The BUILDING prompt says "run tests" generically; AGENTS.md specifies the actual commands. This is how [[backpressure-signals|backpressure]] gets wired in per-project. ([[ralph-playbook]])

## See also

- [[harness-defined]] — the five subsystems (AGENTS.md is the Instructions subsystem)
- [[progressive-disclosure]] — the pattern AGENTS.md should follow
- [[lecture-03-repo-as-system-of-record]] — repo as the single source of truth
- [[cold-start-test]] — the five questions AGENTS.md must answer
- [[ralph-loop]] — where AGENTS.md is loaded every iteration
- [[codegen-as-compiler-output]] — AGENTS.md as natural language is the "PHP of harness"; formal specifications are the next step
- [[process-over-prose]] — AGENTS.md should be workflows with checkpoints, not reference articles
- [[anti-rationalization]] — anti-rationalization tables in AGENTS.md pre-empt the agent's excuses for skipping rules
