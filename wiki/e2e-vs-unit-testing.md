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
