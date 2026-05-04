# Backpressure Signals

**TL;DR** Backpressure is the downstream steering mechanism for autonomous agents — tests, typechecks, lints, and builds that reject invalid work. Without it, the agent has no reason to stop generating broken code. With it, the loop converges on correctness.

## What it means

In the Ralph pattern, you steer the agent from two directions:

- **Upstream** — deterministic setup: the same files loaded every iteration (`PROMPT.md` + `AGENTS.md`), existing code patterns that shape generation, specs that define requirements.
- **Downstream** — backpressure: validation that rejects bad work after it's generated.

Upstream steering is preventive. Backpressure is corrective. You need both.

## Programmatic backpressure

The standard mechanisms: unit tests, integration tests, type checks, linters, builds. The BUILDING prompt says "run tests" generically; `AGENTS.md` specifies the actual commands. This is how backpressure gets wired per-project.

The [[three-layer-termination]] pattern (syntax → tests → e2e) is a specific instance of layered backpressure — each layer catches what the previous one misses.

## Non-deterministic backpressure

Some acceptance criteria resist programmatic validation: writing tone, visual aesthetics, UX quality, content appropriateness. These need human-like judgment but still need backpressure.

**Solution: LLM-as-judge with binary pass/fail.** Create a `createReview()` function in `src/lib/` that takes criteria and an artifact (text or screenshot path), returns `{ pass: boolean, feedback?: string }`. Ralph discovers it during `src/lib` exploration and uses it naturally.

```typescript
const result = await createReview({
  criteria: "Message uses warm, conversational tone",
  artifact: message,
  intelligence: "fast" // or "smart" for nuanced judgment
});
expect(result.pass).toBe(true);
```

LLM reviews are non-deterministic — same artifact may pass one iteration and fail the next. This aligns with Ralph philosophy: eventual consistency through iteration. The loop keeps running until it passes.

## The critical balance

Backpressure must be **specific about WHAT to verify** (outcomes) but **silent on HOW to implement** (approach). Otherwise you're micromanaging the agent, not letting it solve problems.

- ✅ "Extracts 5-10 dominant colors from any uploaded image" (what)
- ❌ "Use K-means clustering with 3 iterations and LAB color space" (how)

## Connection to harness principles

Backpressure is the [[harness-defined|Feedback subsystem]] made operational. Without it, [[overconfidence-bias|the agent's overconfidence]] goes unchecked. The [[sprint-contract]] and [[evaluator-rubric]] are pre-coding ways to define what the backpressure should check; the actual test commands in `AGENTS.md` are how you wire it in.

([[ralph-playbook]])
