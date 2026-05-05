# Clean State Checklist

A session MUST end with all five conditions true:

- [ ] **Build passes** — `npm run build` (or equivalent) succeeds
- [ ] **Tests pass** — `npm test` (or equivalent) is green
- [ ] **Progress recorded** — `PROGRESS.md` is updated with what was done and what's next
- [ ] **No stale artifacts** — no temporary files, debug code, commented-out blocks, or `console.log` left behind
- [ ] **Startup available** — next session can run `bash init.sh` and reach a working state without human help
