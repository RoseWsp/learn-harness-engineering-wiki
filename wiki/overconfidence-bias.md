# Overconfidence Bias

Models systematically report higher confidence than actual accuracy. This is why agents say "done" when they're not.

## What it means

An agent looks at its code and says "this should work." It's not lying — it's reasoning at the token level without runtime feedback. The code looks correct statically, but correctness is a runtime property. ([[lecture-09-premature-victory]])

## The fix

Don't trust the agent's self-assessment. Use external verification:

1. **[[three-layer-termination]]**: Syntax → tests → e2e. All three must pass.
2. **Pass-state gating**: The harness, not the agent, marks features as passing. ([[feature-list]])
3. **Independent evaluator**: A separate agent that verifies the generator's output. ([[lecture-09-premature-victory]])

## The evidence

Anthropic's experiment: single agent says "done" in 20 min, game is broken. Three-agent architecture (planner + generator + evaluator) takes 6 hours but produces a working game. The evaluator's job is specifically to counter overconfidence bias. ([[lecture-09-premature-victory]])

## See also

- [[capability-gap]] — why benchmarks overestimate real-world performance
- [[three-layer-termination]] — the three gates for completion
- [[backpressure-signals]] — downstream verification that counteracts overconfidence
- [[acceptance-driven-backpressure]] — pre-defining "done" before the agent starts
- [[lecture-09-premature-victory]] — the full argument
