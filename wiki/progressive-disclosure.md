# Progressive Disclosure

Overview first, details on demand. The structuring principle for agent instructions.

## What it means

Don't dump 600 lines of instructions on the agent at once. Give a short routing file that links to topic-specific docs. The agent reads what it needs, when it needs it.

This fights two problems: **instruction bloat** (10-15% of context consumed before coding starts) and the **Lost in the Middle Effect** (content in the middle of long contexts is 30-40% less effective). ([[lecture-04-giant-instruction-file-fails]])

## The pattern

```
AGENTS.md (routing, ~80 lines)
├── Overview
├── Quick start
├── Hard constraints
└── Links to topic docs
    ├── api-patterns.md (50-150 lines)
    ├── database-rules.md (50-150 lines)
    └── testing-standards.md (50-150 lines)
```

## Why it works

- Shorter initial context → more budget for actual work
- Higher SNR (signal-to-noise ratio) — the agent only reads relevant rules
- Easier to maintain — update one topic doc without touching the rest
- No Lost in the Middle — each doc is short enough to be fully effective

## Case study

600-line monolithic AGENTS.md → 80-line routing + 3 topic docs → success rate 45% → 72%. ([[lecture-04-giant-instruction-file-fails]])

## See also

- [[agents-md]] — the routing file in practice
- [[lost-in-middle-effect]] — why middle content gets ignored
- [[harness-defined]] — progressive disclosure applies to the Instructions subsystem
- [[subagent-scheduling]] — progressive disclosure at runtime: main context sees only coordination, details loaded on demand via subagents
