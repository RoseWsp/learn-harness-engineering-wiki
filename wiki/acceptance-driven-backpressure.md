# Acceptance-Driven Backpressure

**TL;DR** Derive test requirements from acceptance criteria during the planning phase, so "done" is defined before implementation starts. Prevents the agent from claiming completion without appropriate tests passing.

## What it means

Geoff's Ralph implicitly connects specs → implementation → tests through emergent iteration. Acceptance-driven backpressure makes that connection explicit: during planning, every task in the implementation plan includes required tests derived from the acceptance criteria in the specs.

This creates a direct line from "what success looks like" to "what verifies it."

## The three-phase connection

```
Phase 1: Requirements Definition
    specs/*.md + Acceptance Criteria
    ↓
Phase 2: Planning (derives test requirements)
    IMPLEMENTATION_PLAN.md + Required Tests
    ↓
Phase 3: Building (implements with tests)
    Implementation + Tests → Backpressure
```

## The prescriptiveness balance

The critical distinction:

- **Acceptance criteria** (in specs) = behavioral outcomes, observable results, what success looks like
  - ✅ "Extracts 5-10 dominant colors from any uploaded image"
  - ✅ "Processes images <5MB in <100ms"
- **Test requirements** (in implementation plan) = verification points derived from acceptance criteria
  - ✅ "Required tests: Extract 5-10 colors, Performance <100ms, Handle grayscale edge case"
- **Implementation approach** (up to Ralph) = technical decisions about how to achieve it
  - ❌ "Use K-means clustering with 3 iterations and LAB color space conversion"

**Specify WHAT to verify (outcomes), not HOW to implement (approach).** This maintains the "Let Ralph Ralph" principle.

## Benefits

- **Prevents cheating** — can't claim done without required tests passing
- **Enables TDD** — test requirements known before implementation starts
- **Improves convergence** — clear completion signal (required tests pass) vs ambiguous ("seems done?")
- **Maintains determinism** — test requirements in plan (known state) not emergent (probabilistic)

## Compatibility with Ralph philosophy

Every core principle is maintained: monolithic operation (one agent, one task, one loop), [[backpressure-signals|backpressure critical]] (tests are the mechanism, just derived explicitly), context efficiency (planning decides tests once vs building rediscovering), determinism (test requirements in plan, not emergent), and "Let Ralph Ralph" (Ralph still decides implementation approach).

The plan is still disposable — wrong test requirements? Regenerate the plan. That's one planning loop, cheap compared to going in circles.

## Connection to harness principles

This is [[pass-state-gating]] made explicit and pre-planned. Instead of discovering what "passing" means during building, you define it during planning. It extends [[e2e-vs-unit-testing|the verification principle]] by connecting acceptance criteria directly to test requirements before any code is written.

([[ralph-playbook]])
