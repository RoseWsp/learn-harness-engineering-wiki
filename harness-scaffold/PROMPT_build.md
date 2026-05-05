0a. Read @AGENTS.md for project rules and verification commands.
0b. Read @PROGRESS.md for current state.
0c. Read @IMPLEMENTATION_PLAN.md for the task queue.
0d. Read @feature-list.json for feature states.

1. Select the highest-priority task from @IMPLEMENTATION_PLAN.md that is not yet complete. WIP=1: only one active task at a time.
2. Before making changes, search the codebase to confirm the feature is truly missing. Do not assume.
3. Write failing tests first. "Later" is the most dangerous word — no later.
4. Implement the minimal code to pass the tests.
5. Run ALL three verification layers:
   - Syntax/typecheck: (see AGENTS.md → Validation)
   - Unit tests: (see AGENTS.md → Validation)
   - E2E/integration tests if applicable
6. Only when all three pass:
   - Update @feature-list.json: set `passes: true` for the feature
   - Update @PROGRESS.md: record what was done
   - Update @IMPLEMENTATION_PLAN.md: mark task complete, add findings
   - `git add -A && git commit` with a message describing the changes
   - `git push`

7. If you discover issues unrelated to the current task, add them to @IMPLEMENTATION_PLAN.md — do not scope-creep the current task.

8. When you learn something new about how to run the application, update @AGENTS.md but keep it brief. Status updates and progress notes belong in PROGRESS.md and IMPLEMENTATION_PLAN.md.

9. IMPORTANT: Implement functionality completely. Placeholders and stubs waste future iterations redoing the same work.

10. If all tasks in @IMPLEMENTATION_PLAN.md are complete, stop. Do not invent new scope.
