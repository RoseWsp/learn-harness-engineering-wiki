# Quality Document

An active artifact tracking module quality scores. The A-F grading system for your codebase.

## What it is

Each module gets a quality grade (A through F) based on:

- Build status
- Test pass rate
- Code coverage
- Known defects
- Technical debt level

The quality document is updated at every session end and audited during periodic cleanup. ([[lecture-12-clean-state]])

## Why it matters

Without quality scores, modules silently degrade. A module that was A-grade in week 2 becomes D-grade by week 8, and nobody notices until it breaks. The quality document makes degradation visible. ([[lecture-12-clean-state]])

## Dual-mode cleanup

- **Immediate (per-session)**: Update quality scores for modules you touched
- **Periodic (weekly)**: Re-grade all modules, flag any that dropped

([[lecture-12-clean-state]])

## See also

- [[clean-state-checklist]] — the conditions at session end
- [[harness-rot]] — what happens when quality isn't tracked
- [[lecture-12-clean-state]] — the full argument
