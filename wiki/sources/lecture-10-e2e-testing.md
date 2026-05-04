---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-10-why-end-to-end-testing-changes-results/
raw: raw/docs/en/lectures/lecture-10-why-end-to-end-testing-changes-results/index.md
---

# Lecture 10. Only End-to-End Testing Is True Verification

Unit tests are systematically blind to component interaction issues. E2E is the only verification that matters for the harness.

## What it means

Unit tests verify each component in isolation. They're necessary but insufficient. The bugs that kill you live at the boundaries — interface mismatches, state propagation errors, resource leaks across components. Unit tests can't see these because they mock away the very interactions that break.

## The testing adequacy gradient

Unit < Integration < End-to-End, in terms of defect detection. Each level catches bugs the previous level missed.

## Architectural boundary enforcement

Turn constraints into executable checks, not just documentation. "All API calls must go through the service layer" should be a lint rule, not a comment.

## Review feedback promotion

When you keep writing the same code review comment, promote it to an automated check. The first time is a review; the third time is a missing test.

## Agent-oriented error messages

Same as Lecture 09: when e2e tests fail, the error message should tell the agent exactly what to fix.

## Case study

File export feature with 5 component boundary defects:
- Unit tests: all components pass
- End-to-end tests: catch all 5 defects (interface mismatch, state propagation, resource leak, etc.)

## See also

- [[lecture-09-premature-victory]] — the three-layer termination check
- [[lecture-11-observability]] — runtime observability for debugging
- [[e2e-vs-unit-testing]] — why unit tests miss boundary defects
- [[architectural-boundary-enforcement]] — rules as executable checks
