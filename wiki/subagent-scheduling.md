# Subagent Scheduling

**TL;DR** The main agent context is the most expensive real estate in the loop. Use it as a scheduler — spawn subagents for all real work, keep the main context lean and focused on coordination.

## What it means

In the Ralph pattern, the main agent context serves one purpose: deciding what to do next and coordinating subagents to do it. Every read, search, and investigation is delegated to parallel subagents. The main context stays clean.

This isn't just a style choice — it's forced by the math. A 200K-token window is really ~176K usable, and you want 40-60% utilization for the "smart zone" where reasoning quality peaks. One task per loop already gives you 100% smart zone utilization. But if you fill that zone with file reads and search results, you've wasted it.

## How it works

Each subagent gets its own ~156KB context that's garbage-collected when done. The main agent fans out work to subagents and collects results:

- **Up to 500 parallel Sonnet subagents** for searches/reads
- **1 Sonnet subagent** for build/tests (backpressure control — you want one source of truth for test results)
- **Opus subagents** when complex reasoning is needed (debugging, architectural decisions)

The prompt explicitly controls this: "You may use up to 500 parallel Sonnet subagents for searches/reads and only 1 Sonnet subagent for build/tests."

## Why only 1 subagent for tests?

Multiple test runners create race conditions and conflicting results. One subagent owns the validation step — if it says tests fail, they fail. This is [[backpressure-signals|backpressure]] made concrete.

## The context economics

- Main context: coordination + decision-making + current task
- Subagent contexts: reads, searches, investigations, builds (garbage-collected)
- Shared state: `IMPLEMENTATION_PLAN.md` on disk (persists across iterations)

The plan file replaces what would otherwise be "memory" in the main context. Instead of trying to remember what's done, the agent reads the plan. Instead of trying to remember what's in the codebase, subagents search it fresh each iteration.

## Connection to harness principles

Subagent scheduling is [[progressive-disclosure]] in action: the main context sees only what it needs to make decisions, and details are loaded on demand through subagents. It also prevents [[context-anxiety]] — since the main context stays lean, there's no pressure from an approaching context limit.

([[ralph-playbook]])
