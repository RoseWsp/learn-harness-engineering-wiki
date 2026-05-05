# Harness

Everything in the engineering infrastructure outside the model weights. The five subsystems that make AI coding agents reliable.

## The five subsystems

A harness is not a prompt file. It's five cooperating subsystems, each essential:

1. **Instructions** — what to do, in what order (AGENTS.md, CLAUDE.md)
2. **Tools** — what the agent can use (shell, files, tests)
3. **Environment** — where it runs (dependencies, services, versions)
4. **State** — what's been done (PROGRESS.md, git history, [[feature-list]])
5. **Feedback** — whether it worked (test/lint/build results)

Leave any out and reliability drops. ([[lecture-02-what-harness-actually-is]])

## The kitchen analogy

| Subsystem | Kitchen | Harness |
|-----------|---------|---------|
| Instructions | Recipe shelf | AGENTS.md |
| Tools | Knife rack | Shell, tests |
| Environment | Stove | Deps, versions |
| State | Prep station | PROGRESS.md, git |
| Feedback | Quality window | Test results |

## ROI ranking

Adding subsystems incrementally, success rate: 20% → 60% (instructions) → 80% (feedback) → 80-100% (state). **Feedback has the highest ROI.** ([[lecture-02-what-harness-actually-is]])

## Harness rot

Harnesses degrade like code. Rules go stale, constraints become outdated as models improve. Audit regularly, delete what's no longer needed. ([[lecture-12-clean-state]])

## The core evidence

Anthropic's controlled experiment: same model (Opus 4.5), same prompt. Without harness: 20 min, $9, broken. With harness: 6 hours, $200, fully playable. OpenAI: Codex in a well-harnessed repo goes from "unreliable" to "reliable" — a qualitative shift. ([[lecture-01-capable-agents-still-fail]])

## See also

- [[agents-md]] — the instructions subsystem in detail
- [[feature-list]] — the state subsystem's key data structure
- [[e2e-vs-unit-testing]] — the feedback subsystem's most impactful layer
- [[progressive-disclosure]] — how to structure instructions without bloat
- [[ralph-loop]] — a concrete implementation of all five subsystems as a bash loop
- [[backpressure-signals]] — the feedback subsystem made operational: tests, lints, and LLM-as-judge
- [[sandbox-for-agents]] — the environment subsystem's security boundary
- [[anti-rationalization]] — pre-empting the agent's self-justification for skipping rules
- [[process-over-prose]] — instructions should be workflows, not reference docs
