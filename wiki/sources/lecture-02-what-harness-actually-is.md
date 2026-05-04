---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-02-what-a-harness-actually-is/
raw: raw/docs/en/lectures/lecture-02-what-a-harness-actually-is/index.md
---

# Lecture 02. What a Harness Actually Is

A harness is five subsystems, not a prompt file. Leave any out and reliability drops.

## The kitchen analogy

Think of a harness like a professional kitchen:

| Subsystem | Kitchen | Harness |
|-----------|---------|---------|
| Instructions | Recipe shelf | AGENTS.md / CLAUDE.md |
| Tools | Knife rack | Shell, files, tests |
| Environment | Stove & oven | Dependencies, services, versions |
| State | Prep station | PROGRESS.md, git history |
| Feedback | Quality check window | Test/lint/build results |

All five are essential. A kitchen without a stove can't cook; an agent without verification can't know if it's right.

## Core principles

- **Repo as single source of truth**: If the agent can't see it, it doesn't exist. ([[lecture-03-repo-as-record]])
- **Give a map, not a manual**: AGENTS.md should be a directory page (~100 lines), not a 600-line wall of text. ([[lecture-04-giant-file-fails]])
- **Constrain, don't micromanage**: Executable rules beat enumerating every step.
- **Isometric model control**: Remove subsystems one at a time to measure each one's impact.
- **Harness rots like code**: Audit regularly.

## ROI ranking

Adding subsystems incrementally, success rate jumps:

1. Empty kitchen (no harness): 20%
2. + Instructions (recipe shelf): 60%
3. + Feedback (quality check): 80%
4. + State (prep station): 80–100%

**Feedback has the highest ROI.** Verification commands are the single most impactful thing you can add.

## Key terms

- **Five Subsystems**: Instructions, Tools, Environment, State, Feedback
- **Isometric Control**: Remove one subsystem at a time to measure its contribution
- **Harness Rot**: Harness quality degrades over time without maintenance

## See also

- [[lecture-01-capable-agents-still-fail]] — why capable agents fail without a harness
- [[harness-defined]] — the full definition
- [[lecture-09-premature-victory]] — feedback subsystem in action
- [[agents-md]] — the instructions subsystem
