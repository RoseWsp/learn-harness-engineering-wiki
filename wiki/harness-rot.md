# Harness Rot

Harnesses degrade like code. Without regular audits, they accumulate stale rules and outdated constraints.

## What it means

Three forms of decay:

1. **Rule accumulation** — rules are added but never removed (the vicious cycle from [[lecture-04-giant-instruction-file-fails]])
2. **Model improvement** — constraints needed for GPT-3.5 may be over-constraining for Opus 4.5
3. **Stale state** — PROGRESS.md not updated, feature lists drift from reality

## The vicious cycle

Agent makes mistake → add rule → works temporarily → another mistake → another rule → file bloats. Each new rule makes all the others harder to follow. ([[lecture-04-giant-instruction-file-fails]])

## How to fight it

- **Audit regularly**: Review every rule — does it still matter?
- **Delete aggressively**: If a rule hasn't been triggered in a month, remove it
- **Add expiry conditions**: Every rule should state when it can be removed
- **Simplify as models improve**: Remove constraints that newer models handle natively

([[lecture-12-clean-state]])

## See also

- [[lecture-04-giant-instruction-file-fails]] — the vicious cycle
- [[lecture-12-clean-state]] — cleanup as a harness maintenance practice
- [[agents-md]] — each rule should have an expiry condition
- [[progressive-disclosure]] — structure that makes rot visible
