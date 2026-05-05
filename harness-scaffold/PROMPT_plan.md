0a. Read @AGENTS.md for project rules and verification commands.
0b. Read @PROGRESS.md for current state.
0c. Read `specs/*` to learn the application specifications.
0d. Read @IMPLEMENTATION_PLAN.md (if present) to understand the plan so far.
0e. Read the source code to understand existing implementation.

1. Compare existing code against `specs/*`. Identify gaps: missing features, stubs, TODOs, skipped tests, inconsistent patterns. Use subagents for parallel searches.
2. Create or update @IMPLEMENTATION_PLAN.md as a prioritized bullet-point list. Each item must include:
   - Feature ID (matching `feature-list.json`)
   - Description of what's missing
   - Verification command
   - Dependencies on other items
3. Prioritize: blocked features last, highest-value features first.

IMPORTANT: Plan only. Do NOT implement anything. Do NOT assume functionality is missing — confirm with code search first. Treat the plan as the single source of truth for what remains to be done.
