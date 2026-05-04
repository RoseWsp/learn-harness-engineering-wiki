---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-09-why-agents-declare-victory-too-early/
raw: raw/docs/en/lectures/lecture-09-why-agents-declare-victory-too-early/index.md
---

# Lecture 09. Agents Declare Victory Too Early

Agents rely on local code confidence, not system-level verification. They overestimate completion.

## What it means

Models have an **overconfidence bias** — they systematically report higher confidence than actual accuracy. An agent says "done" because the code looks right, not because it actually runs. This isn't dishonesty; it's a fundamental limitation of token-level reasoning without runtime feedback.

## The three-layer termination check

Don't accept "done" from the agent. Run three independent layers:

1. **Syntax / static analysis** — does the code compile? Lint clean?
2. **Runtime behavior verification** — do unit tests pass? Does the feature work in isolation?
3. **System-level end-to-end testing** — does the whole system work end-to-end?

Only when all three pass is the agent actually done.

## The verification-validation dual gate

- **Verification**: Is the code correct? (tests, lint, type-check)
- **Validation**: Does the system behave correctly? (end-to-end, user flow)

Both gates must open before declaring completion.

## Independent evaluator

The most powerful pattern: a separate agent for evaluation, tuned to be "picky." The generator writes code; the evaluator independently verifies. This is the planner + generator + evaluator architecture from Anthropic's experiment.

## Agent-oriented error messages

When verification fails, don't just say "test failed." Include specific fix instructions: which file, which function, what to change. The agent should be able to fix the issue without detective work.

## Case study

Anthropic's controlled experiment (same as Lecture 01):
- **Single agent**: 20 mins, $9, game entities unresponsive
- **Three agents (Planner + Generator + Evaluator)**: 6 hours, $200, fully playable game

The model didn't change. The harness did.

## See also

- [[lecture-01-capable-agents-still-fail]] — the same Anthropic experiment from the failure perspective
- [[lecture-10-e2e-testing]] — why only end-to-end testing is true verification
- [[lecture-08-feature-lists]] — pass-state gating prevents self-grading
- [[overconfidence-bias]] — models systematically overestimate accuracy
- [[three-layer-termination]] — the three gates for completion
