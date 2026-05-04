---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-04-why-one-giant-instruction-file-fails/
raw: raw/docs/en/lectures/lecture-04-why-one-giant-instruction-file-fails/index.md
---

# Lecture 04. Why One Giant Instruction File Fails

A 600-line AGENTS.md is worse than a 60-line one. The bigger the file, the less the agent follows.

## The vicious cycle

Agent makes a mistake → you add a rule to AGENTS.md → it works temporarily → another mistake → another rule → the file bloats. Each new rule makes all the others harder to follow.

## Why big files fail

Five specific problems:

1. **Context budget eaten** — 10-15% of the context window consumed before coding starts
2. **Lost in the Middle** — Liu et al. (2023): content in the middle of a long context is 30-40% less effective. Rules in the middle are essentially ignored.
3. **Priority ambiguity** — all rules look equally important, so none stand out
4. **Maintenance decay** — the file only grows; rules are added but never removed
5. **Contradictions** — conflicting rules accumulate, and the agent picks randomly

## The solution: routing file + progressive disclosure

- **AGENTS.md** (50-200 lines): overview, quick start, hard constraints, topic links
- **Topic docs** (50-150 lines each): API patterns, database rules, testing standards
- **Each rule**: source, applicability, expiry condition

The agent reads the routing file, then follows links to only the relevant topic docs. Progressive disclosure: overview first, details when needed.

## Key terms

- **Instruction Bloat**: >10-15% of context budget occupied by instructions
- **SNR (Signal-to-Noise Ratio)**: Relevant instructions per task — bloat kills SNR
- **Routing File**: Short AGENTS.md pointing to topic docs
- **Progressive Disclosure**: Overview first, details on demand
- **Lost in the Middle Effect**: LLMs struggle with information in the middle of long contexts

## Case study

600-line monolithic AGENTS.md → 80-line routing file + 3 topic docs → success rate 45% → 72%, security compliance 60% → 95%.

## See also

- [[agents-md]] — how to write a good AGENTS.md
- [[lecture-03-repo-as-system-of-record]] — repo as source of truth
- [[progressive-disclosure]] — the pattern of overview-first
- [[lost-in-middle-effect]] — why middle content gets ignored
- [[lecture-02-what-harness-actually-is]] — the instructions subsystem
