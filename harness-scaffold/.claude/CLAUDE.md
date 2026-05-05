# Harness Configuration

## Working Directory

Root of repository.

## Harness Rules

### 1. WIP=1 Constraint
Only one active feature at a time. No new feature can start if any feature is `passes: false` and in progress.

### 2. Pass-State Gating
The agent cannot mark features as "passing" on its own say-so. Only passing test evidence (all three layers) justifies setting `passes: true` in `feature-list.json`.

### 3. Three-Layer Termination
All changes must pass before commit:
- **Layer 1**: Syntax / typecheck / lint
- **Layer 2**: Unit tests
- **Layer 3**: E2E / integration tests

### 4. Clean State
Sessions must end with ALL five conditions met (see `docs/clean-state-checklist.md`):
1. Build passes
2. Tests pass
3. PROGRESS.md updated
4. No stale artifacts (debug code, commented blocks, temp files)
5. Next session can start without human help

### 5. Anti-Rationalization
When the agent generates an excuse for skipping a rule, consult the Anti-Rationalization Table in `AGENTS.md`. The rebuttal is pre-written. Follow it.

### 6. Process Over Prose
Instructions are workflows with checkpoints and exit criteria — not reference articles. Follow the steps in order. Produce verifiable evidence at each checkpoint.

## Verification Commands

<!-- FILL IN: your project's commands -->
```
Build:      npm run build
Typecheck:  npm run typecheck
Test:       npm test
Lint:       npm run lint
E2E:        npm run test:e2e
```

## Session Protocol

### Clock In
```bash
bash init.sh
```
Read PROGRESS.md → Read IMPLEMENTATION_PLAN.md → Pick top task → Go.

### Clock Out
1. Update PROGRESS.md
2. Update feature-list.json
3. Update IMPLEMENTATION_PLAN.md
4. Verify clean state (5 conditions)
5. Commit and push
