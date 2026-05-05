# Three-Layer Termination

The three verification gates an agent must pass before work is considered done.

## The three layers

1. **Syntax / static analysis** — does the code compile? Lint clean? Type-check pass?
2. **Runtime behavior** — do unit tests pass? Does the feature work in isolation?
3. **System-level e2e** — does the whole system work end-to-end?

Only when all three pass is the agent actually done. Accepting "done" at layer 1 or 2 is how [[overconfidence-bias]] kills you. ([[lecture-09-premature-victory]])

## Why all three

Unit tests (layer 2) are systematically blind to component interaction issues. Interface mismatches, state propagation errors, resource leaks — these live at the boundaries between components. Only e2e tests (layer 3) catch them. ([[lecture-10-e2e-testing]])

## The verification-validation dual gate

- **Verification**: Is the code correct? (layers 1-2)
- **Validation**: Does the system behave correctly? (layer 3)

Both gates must open. ([[lecture-09-premature-victory]])

## Agent-oriented error messages

When any layer fails, the error message should tell the agent exactly what to fix: which file, which function, what to change. No detective work. ([[lecture-09-premature-victory]], [[lecture-10-e2e-testing]])

## See also

- [[e2e-vs-unit-testing]] — why layer 3 catches what layer 2 misses
- [[overconfidence-bias]] — why agents skip layers
- [[pass-state-gating]] — the harness enforces termination
- [[backpressure-signals]] — the downstream mechanisms that implement each layer
- [[ralph-loop]] — three-layer termination in the Ralph pattern: commit only when tests pass
- [[anti-rationalization]] — pre-empting the agent's excuses for skipping layers
- [[agent-skills-osmani]] — Osmani: "verification is non-negotiable; 'looks right' is never enough"
- [[lecture-09-premature-victory]] — the full argument
