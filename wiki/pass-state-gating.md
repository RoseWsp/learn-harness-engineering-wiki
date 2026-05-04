# Pass-State Gating

Only the harness can mark a feature as "passing." The agent cannot grade its own homework.

## What it means

In the [[feature-list]], features transition through states: not_started → active → blocked → passing. The "passing" transition is gated — it requires the harness to independently run verification and confirm the feature works. The agent cannot self-promote a feature to passing. ([[lecture-08-feature-lists]])

## Why it matters

Without pass-state gating, agents mark features as "done" based on code inspection, not runtime verification. This is [[overconfidence-bias]] in action. The agent looks at the code, it looks right, so it marks it done. But "looking right" ≠ "running right." ([[lecture-09-premature-victory]])

## How it works

1. Agent marks feature "active" and implements it
2. Agent runs the verification command specified in the feature list
3. If verification passes, the harness (or the agent following harness rules) marks the feature "passing"
4. Only then can the next feature be started ([[wip-limit]])

## See also

- [[feature-list]] — the data structure with states
- [[overconfidence-bias]] — why self-grading fails
- [[three-layer-termination]] — the verification that must pass
- [[acceptance-driven-backpressure]] — pre-defining what "passing" means before implementation
- [[ralph-loop]] — pass-state gating via the plan file: only updated after tests pass
- [[lecture-08-feature-lists]] — the full argument
