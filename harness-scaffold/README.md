# Harness Scaffold

A ready-to-use harness engineering scaffold for AI coding agents. Drop it into any project and start coding with reliability.

Based on the [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/) course and the [Ralph pattern](https://github.com/nichochar/ralph-wiggum) by Geoffrey Huntley.

## Quick Start

```bash
# 1. Copy scaffold into your project
cp -r harness-scaffold/* /your-project/

# 2. Fill in the REPLACE placeholders
#    - AGENTS.md: build/run/test commands
#    - feature-list.json: your features
#    - specs/: your requirements
#    - docs/api-patterns.md: your API rules
#    - .claude/CLAUDE.md: your verification commands

# 3. Initialize
bash init.sh

# 4. Start the Ralph loop
./loop.sh        # build mode (unlimited)
./loop.sh plan   # plan mode first, then build
```

## What You Get

```
your-project/
├── AGENTS.md                  # Agent routing guide (read this first)
├── feature-list.json          # Scope control + verification
├── PROGRESS.md                # Session journal (clock-in/clock-out)
├── IMPLEMENTATION_PLAN.md     # Prioritized task queue
├── init.sh                    # Bootstrap verification script
├── loop.sh                    # Ralph loop (plan + build modes)
├── PROMPT_plan.md             # Planning-mode prompt
├── PROMPT_build.md            # Building-mode prompt
├── .claude/
│   └── CLAUDE.md              # Harness rules for Claude Code
├── docs/
│   ├── clean-state-checklist.md
│   ├── sprint-contract.md
│   ├── evaluator-rubric.md
│   ├── quality-document.md
│   ├── testing-standards.md
│   └── api-patterns.md
└── specs/                     # Your requirements go here
```

## The Five Harness Subsystems

| Subsystem | File(s) | Purpose |
|---|---|---|
| **Instructions** | `AGENTS.md`, `.claude/CLAUDE.md` | What the agent should do |
| **Tools** | `loop.sh`, `init.sh` | How the agent operates |
| **Environment** | `specs/`, `docs/` | Context the agent needs |
| **State** | `PROGRESS.md`, `feature-list.json`, `IMPLEMENTATION_PLAN.md` | What's been done, what's next |
| **Feedback** | Three-layer verification (syntax → tests → e2e) | Evidence that it works |

## Key Workflows

### Session Lifecycle

```
bash init.sh          ← Clock in: verify bootstrap contract
     ↓
Read PROGRESS.md      ← Orient: where are we?
     ↓
Read IMPLEMENTATION_PLAN.md  ← Pick: what's next?
     ↓
Implement (WIP=1)     ← Work: one feature at a time
     ↓
Run all 3 layers      ← Verify: syntax → unit → e2e
     ↓
Update files          ← Record: progress, features, plan
     ↓
Commit + push         ← Save: clean state only
```

### Ralph Loop

```
./loop.sh plan        ← Generate IMPLEMENTATION_PLAN.md from specs
./loop.sh             ← Build: one iteration per loop tick
./loop.sh 10          ← Build with max 10 iterations
```

Each iteration starts with **fresh context** — no context anxiety, no stale assumptions. The plan file on disk is the only shared state between iterations.

## Core Principles

1. **WIP=1** — One feature at a time. No exceptions.
2. **Pass-state gating** — Only passing tests mark features as done. No self-grading.
3. **Three-layer termination** — Syntax → unit tests → e2e. All must pass.
4. **Clean state** — Sessions end with build green, tests green, progress recorded, no artifacts.
5. **Anti-rationalization** — When the agent makes an excuse, the rebuttal is pre-written.
6. **Process over prose** — Instructions are workflows with checkpoints, not reference articles.

## Customization Checklist

Before first use, replace every `REPLACE` placeholder:

- [ ] `AGENTS.md` → Build, run, test commands
- [ ] `AGENTS.md` → Anti-rationalization table (project-specific excuses)
- [ ] `feature-list.json` → Your actual features
- [ ] `IMPLEMENTATION_PLAN.md` → Your actual tasks
- [ ] `specs/` → Your requirements documents
- [ ] `.claude/CLAUDE.md` → Your verification commands
- [ ] `docs/api-patterns.md` → Your API rules
- [ ] `docs/testing-standards.md` → Your coverage targets
- [ ] `docs/quality-document.md` → Your modules
- [ ] `init.sh` → Adjust checks for your tech stack
