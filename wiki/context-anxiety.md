# Context Anxiety

When context windows run low, agents rush to premature completion. Different models handle it differently.

## What it means

Context windows are finite. As the agent approaches the limit, it experiences "anxiety" — a behavioral shift toward rushing. Instead of completing work thoroughly, it declares "done" early to avoid running out of space. ([[lecture-05-continuity]])

## Model differences

- **Sonnet 4.5**: Severe anxiety — needs explicit context reset
- **Opus 4.5**: Mild anxiety — compaction works, can continue with reduced context

The fix isn't a bigger context window (though that helps). The fix is structured state persistence — [[progress-md]], [[feature-list]], git checkpoints — so the agent knows it can pick up where it left off in a new session. ([[lecture-05-continuity]])

## Long-running amplification

Context anxiety is a *rate* problem — the longer the session, the more it compounds. Osmani frames this sharply: "A 10-minute agent that skips tests creates a bug. A 30-hour agent that skips tests creates an archaeological debugging project." The longer the run, the more senior-engineer scaffolding must be *enforced* rather than *suggested*. Short sessions survive on discipline; long sessions require structure. ([[agent-skills-osmani]])

## Related

- [[overconfidence-bias]] — agents also overestimate completion
- [[ralph-loop]] — context anxiety eliminated by design: each iteration starts with fresh context
- [[subagent-scheduling]] — keeping the main context lean avoids anxiety triggers
- [[lecture-05-continuity]] — the full argument on continuity artifacts
- [[lecture-09-premature-victory]] — premature completion as a harness problem
- [[agent-skills-osmani]] — long-running agents amplify every shortcut
