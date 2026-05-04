---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/
raw: raw/docs/en/lectures/lecture-03-why-the-repository-must-become-the-system-of-record/index.md
---

# Lecture 03. The Repository Must Become the System of Record

Knowledge not in the repo doesn't exist for agents. The repo must be the authoritative source.

## What it means

Scattered knowledge is invisible knowledge. Confluence pages go stale. Slack messages can't be searched by agents. Tribal knowledge in people's heads doesn't scale. Jira tickets the agent can't see. If it's not in the repo, it's not in the agent's world.

## The Cold-Start Test

Can a fresh agent session answer five basic questions about your project?

1. What does this project do?
2. How do I run it?
3. How do I test it?
4. What's the current state of work?
5. Where do I find X?

If it can't, your knowledge is scattered. The cost shows up as **discovery cost** — context budget burned just finding information before any real work starts.

## Key concepts

- **Knowledge Visibility Gap**: Proportion of project knowledge not in the repo
- **System of Record**: The repo has the final word on decisions and architecture
- **Cold-Start Test**: Five questions a fresh session should answer
- **Discovery Cost**: Context budget burned finding info (target: near zero)
- **Knowledge Decay Rate**: How fast out-of-repo info becomes stale

## The ACID analogy for state

Treat agent state like database transactions:

- **Atomic**: Changes are all-or-nothing (git commits)
- **Consistent**: Progress files always reflect reality
- **Isolated**: Sessions don't interfere with each other
- **Durable**: State survives crashes and context resets

## What to do

1. **Knowledge near code** — ARCHITECTURE.md per module, not a wiki
2. **Standardized AGENTS.md** — 50-100 lines, landing page for the agent
3. **Minimal but complete** — pass the Cold-Start Test
4. **Update with code** — CI reminders, not manual wiki gardening
5. **ACID state management** — git commits + progress files

## Case study

E-commerce platform: scattered decisions across Confluence/Slack → AGENTS.md + per-service ARCHITECTURE.md + PROGRESS.md → human intervention drops from 70% to 0%.

## See also

- [[agents-md]] — the landing page for agents
- [[lecture-02-what-harness-actually-is]] — the five subsystems
- [[lecture-05-continuity]] — state persistence across sessions
- [[cold-start-test]] — the five-question test
- [[lecture-04-giant-file-fails]] — why a single giant file isn't the answer
