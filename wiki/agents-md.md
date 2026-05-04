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
