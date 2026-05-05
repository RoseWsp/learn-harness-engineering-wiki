# E2E vs Unit Testing

Unit tests verify components in isolation. E2E tests verify the system as a whole. The bugs that kill you live at the boundaries.

## The testing adequacy gradient

Unit < Integration < End-to-End, in terms of defect detection. Each level catches bugs the previous level missed. ([[lecture-10-e2e-testing]])

## What unit tests miss

Component boundary defects — issues at the interfaces between components:

- **Interface mismatch**: Component A calls Component B with wrong parameters
- **State propagation**: State changes in A aren't reflected in B
- **Resource leaks**: A resource opened in one layer isn't closed in another
- **Event ordering**: Events arrive in an order the system doesn't handle
- **Configuration drift**: Different components expect different configs

Unit tests mock away these very interactions. They're necessary but insufficient for harness verification. ([[lecture-10-e2e-testing]])

## Google-scale testing practices

Two practices from *Software Engineering at Google* directly reinforce the testing adequacy gradient:

- **Beyoncé Rule**: "If you liked it, you should have put a test on it." Infrastructure changes won't catch bugs — tests will. If a behavior isn't tested, it's not guaranteed, and the first infrastructure change that breaks it is *your* fault, not the change author's.
- **DAMP > DRY in tests**: Test code should be readable as specification, even at the cost of some duplication. Over-abstracted test helpers are a known anti-pattern — they obscure what's being tested and make failures harder to diagnose. Descriptive And Meaningful Phrases beat Don't Repeat Yourself in the test layer.

Both practices reinforce the [[three-layer-termination]] model: the Beyoncé Rule is why layer 3 exists (untested boundaries are unsupported boundaries), and DAMP > DRY ensures each test is legible enough to serve as a verification checkpoint. ([[agent-skills-osmani]])

## What the harness requires

The harness should require e2e tests for any cross-component change. This is the [[three-layer-termination]] in action — layer 3 is non-negotiable.

## Case study

File export feature with 5 boundary defects:
- Unit tests: all components pass
- E2E tests: catch all 5 defects ([[lecture-10-e2e-testing]])

## See also

- [[three-layer-termination]] — the three verification gates
- [[backpressure-signals]] — how e2e tests become backpressure in the agent loop
- [[acceptance-driven-backpressure]] — deriving test requirements from acceptance criteria
- [[lecture-10-e2e-testing]] — the full argument
- [[harness-defined]] — e2e testing as part of the Feedback subsystem
- [[agent-skills-osmani]] — Beyoncé Rule, DAMP > DRY: Google testing practices for agents
