# Harness Engineering Wiki

The strongest model in the world will still fail on real tasks if you don't build a proper environment around it. This wiki captures the principles and practices of harness engineering — the discipline of making AI coding agents reliable.

```svg
<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg" font-family="system-ui, sans-serif">
  <!-- Title -->
  <text x="400" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#1a1a2e">The Harness Pattern</text>

  <!-- Agent box -->
  <rect x="320" y="50" width="160" height="40" rx="8" fill="#6c5ce7" opacity="0.9"/>
  <text x="400" y="75" text-anchor="middle" font-size="13" fill="white" font-weight="bold">AI Agent</text>

  <!-- Arrow down -->
  <line x1="400" y1="90" x2="400" y2="120" stroke="#6c5ce7" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Harness box -->
  <rect x="150" y="120" width="500" height="40" rx="8" fill="#00b894" opacity="0.15" stroke="#00b894" stroke-width="1.5"/>
  <text x="400" y="145" text-anchor="middle" font-size="13" fill="#00b894" font-weight="bold">HARNESS governs every step</text>

  <!-- Five subsystems -->
  <g transform="translate(0, 180)">
    <!-- Instructions -->
    <rect x="50" y="0" width="130" height="70" rx="8" fill="#fd79a8" opacity="0.15" stroke="#fd79a8" stroke-width="1.5"/>
    <text x="115" y="25" text-anchor="middle" font-size="11" fill="#fd79a8" font-weight="bold">Instructions</text>
    <text x="115" y="42" text-anchor="middle" font-size="10" fill="#555">AGENTS.md</text>
    <text x="115" y="57" text-anchor="middle" font-size="10" fill="#555">CLAUDE.md</text>

    <!-- Tools -->
    <rect x="195" y="0" width="130" height="70" rx="8" fill="#e17055" opacity="0.15" stroke="#e17055" stroke-width="1.5"/>
    <text x="260" y="25" text-anchor="middle" font-size="11" fill="#e17055" font-weight="bold">Tools</text>
    <text x="260" y="42" text-anchor="middle" font-size="10" fill="#555">Shell</text>
    <text x="260" y="57" text-anchor="middle" font-size="10" fill="#555">Files / Tests</text>

    <!-- Environment -->
    <rect x="340" y="0" width="130" height="70" rx="8" fill="#fdcb6e" opacity="0.15" stroke="#fdcb6e" stroke-width="1.5"/>
    <text x="405" y="25" text-anchor="middle" font-size="11" fill="#b8860b" font-weight="bold">Environment</text>
    <text x="405" y="42" text-anchor="middle" font-size="10" fill="#555">Deps / Versions</text>
    <text x="405" y="57" text-anchor="middle" font-size="10" fill="#555">Services</text>

    <!-- State -->
    <rect x="485" y="0" width="130" height="70" rx="8" fill="#74b9ff" opacity="0.15" stroke="#74b9ff" stroke-width="1.5"/>
    <text x="550" y="25" text-anchor="middle" font-size="11" fill="#0984e3" font-weight="bold">State</text>
    <text x="550" y="42" text-anchor="middle" font-size="10" fill="#555">PROGRESS.md</text>
    <text x="550" y="57" text-anchor="middle" font-size="10" fill="#555">Feature Lists</text>

    <!-- Feedback -->
    <rect x="630" y="0" width="130" height="70" rx="8" fill="#00b894" opacity="0.15" stroke="#00b894" stroke-width="1.5"/>
    <text x="695" y="25" text-anchor="middle" font-size="11" fill="#00b894" font-weight="bold">Feedback</text>
    <text x="695" y="42" text-anchor="middle" font-size="10" fill="#555">Test / Lint</text>
    <text x="695" y="57" text-anchor="middle" font-size="10" fill="#555">Build results</text>
  </g>

  <!-- Connecting lines from harness to subsystems -->
  <line x1="400" y1="160" x2="115" y2="180" stroke="#aaa" stroke-width="1" stroke-dasharray="4"/>
  <line x1="400" y1="160" x2="260" y2="180" stroke="#aaa" stroke-width="1" stroke-dasharray="4"/>
  <line x1="400" y1="160" x2="405" y2="180" stroke="#aaa" stroke-width="1" stroke-dasharray="4"/>
  <line x1="400" y1="160" x2="550" y2="180" stroke="#aaa" stroke-width="1" stroke-dasharray="4"/>
  <line x1="400" y1="160" x2="695" y2="180" stroke="#aaa" stroke-width="1" stroke-dasharray="4"/>

  <!-- Result -->
  <g transform="translate(0, 280)">
    <rect x="250" y="0" width="300" height="40" rx="8" fill="#1a1a2e" opacity="0.9"/>
    <text x="400" y="25" text-anchor="middle" font-size="12" fill="white" font-weight="bold">Agent stops only when verification passes</text>
  </g>

  <!-- Key principles -->
  <g transform="translate(0, 340)">
    <rect x="50" y="0" width="220" height="70" rx="8" fill="none" stroke="#ddd" stroke-width="1"/>
    <text x="160" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a1a2e">Scope Control</text>
    <text x="160" y="38" text-anchor="middle" font-size="10" fill="#555">WIP=1, Feature Lists</text>
    <text x="160" y="53" text-anchor="middle" font-size="10" fill="#555">Pass-state Gating</text>

    <rect x="290" y="0" width="220" height="70" rx="8" fill="none" stroke="#ddd" stroke-width="1"/>
    <text x="400" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a1a2e">Verification</text>
    <text x="400" y="38" text-anchor="middle" font-size="10" fill="#555">E2E Testing</text>
    <text x="400" y="53" text-anchor="middle" font-size="10" fill="#555">Three-Layer Termination</text>

    <rect x="530" y="0" width="220" height="70" rx="8" fill="none" stroke="#ddd" stroke-width="1"/>
    <text x="640" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a1a2e">Continuity</text>
    <text x="640" y="38" text-anchor="middle" font-size="10" fill="#555">PROGRESS.md, init.sh</text>
    <text x="640" y="53" text-anchor="middle" font-size="10" fill="#555">Clean State Handoff</text>
  </g>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#6c5ce7"/>
    </marker>
  </defs>
</svg>
```

## The core argument

**The model is smart. The harness makes it reliable.** Anthropic ran a controlled experiment: same model (Opus 4.5), same prompt. Without a harness: 20 min, $9, broken result. With a harness: 6 hours, $200, fully working. OpenAI reported the same — Codex goes from "unreliable" to "reliable" with proper harness engineering. Not a marginal improvement — a qualitative shift. ([[lecture-01-capable-agents-still-fail]])

## The five subsystems

A harness is not a prompt file. It's five cooperating subsystems: [[agents-md|Instructions]], Tools, Environment, [[progress-md|State]], and [[e2e-vs-unit-testing|Feedback]]. Leave any out and reliability drops. [[harness-defined|Feedback has the highest ROI]] — verification commands are the single most impactful thing you can add. ([[lecture-02-what-harness-actually-is]])

## Where agents fail

Six failure patterns, all harness-induced: underspecified tasks, implicit conventions, broken environments, no verification, [[context-anxiety]], lost continuity. The fix is the [[diagnostic-loop]]: attribute failures to a layer, fix it, measure. ([[lecture-01-capable-agents-still-fail]])

## The instruction problem

A 600-line AGENTS.md is worse than a 60-line one. The [[lost-in-middle-effect]] means rules in the middle are ignored. The fix is [[progressive-disclosure]]: a short routing file linking to topic docs. ([[lecture-04-giant-instruction-file-fails]])

## Scope and completion

Agents overreach (start 5 features, finish 0) and under-finish (declare victory too early). [[wip-limit|WIP=1]] prevents overreach. [[pass-state-gating]] prevents self-grading. [[three-layer-termination|Three-layer verification]] catches what the agent misses. ([[lecture-07-task-boundaries]], [[lecture-08-feature-lists]], [[lecture-09-premature-victory]])

## Continuity and state

Sessions are finite. Without [[progress-md|structured state persistence]], every session starts from scratch. The [[cold-start-test]] measures how fast a new session can orient. The [[clean-state-checklist]] ensures each session ends well. ([[lecture-05-continuity]], [[lecture-12-clean-state]])

## Observability

Without runtime signals and process artifacts, agents make decisions under uncertainty. [[sprint-contract|Sprint contracts]] and [[evaluator-rubric|evaluator rubrics]] turn subjective evaluation into quantifiable metrics. ([[lecture-11-observability]])

## How to train

Reading about harness engineering isn't enough — you need to build the environments yourself and observe how agents behave under different rules. The [[harness-deliberate-practice]] guide is a 6-week progressive program: each week adds one harness subsystem, every exercise runs as a controlled experiment (with harness vs. without), and the final week is an ablation study that shows which components actually matter. The core training principle: **when the agent fails, don't fix the code — fix the harness.**

## A concrete implementation: the Ralph pattern

The principles above aren't just theory. The [[ralph-loop|Ralph pattern]] (by Geoffrey Huntley, documented in the [[ralph-playbook]]) is a working implementation of most harness principles in one simple mechanism: a dumb bash loop that restarts an LLM agent with fresh context, using a plan file on disk as the only shared state.

**How Ralph maps to the harness:**

- [[wip-limit|WIP=1]] — one task per loop iteration
- [[pass-state-gating]] — only the plan file marks tasks done (after tests pass)
- [[three-layer-termination|Three-layer verification]] — commit only when tests pass
- [[progressive-disclosure]] — short AGENTS.md (~60 lines), not a 600-line manual
- [[backpressure-signals|Backpressure]] — tests, lints, and builds reject bad work downstream
- [[subagent-scheduling|Subagent scheduling]] — main context as coordinator, subagents as memory extension
- [[context-anxiety|Context anxiety]] — eliminated by design: each iteration starts fresh

The key insight: **context is everything.** A 200K-token window is ~176K usable; tight tasks + one task per loop = 100% smart zone utilization. The main agent becomes a scheduler, subagents do the real work. Upstream steering (deterministic setup) + downstream backpressure (tests reject bad work) = convergence. And [[sandbox-for-agents|sandboxing]] is non-negotiable when `--dangerously-skip-permissions` is required for autonomy.

Further refinements: [[acceptance-driven-backpressure|acceptance-driven backpressure]] derives test requirements from specs before implementation, and [[story-map-slc|story mapping]] frames product scope as user journeys sliced into Simple/Lovable/Complete releases.

## Sources

This wiki is based on the [Learn Harness Engineering](https://walkinglabs.github.io/learn-harness-engineering/) course by WalkingLabs, which synthesizes research from [OpenAI](https://openai.com/index/harness-engineering/) and [Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).

[[lecture-01-capable-agents-still-fail]] · [[lecture-02-what-harness-actually-is]] · [[lecture-03-repo-as-system-of-record]] · [[lecture-04-giant-instruction-file-fails]] · [[lecture-05-continuity]] · [[lecture-06-initialization-phase]] · [[lecture-07-task-boundaries]] · [[lecture-08-feature-lists]] · [[lecture-09-premature-victory]] · [[lecture-10-e2e-testing]] · [[lecture-11-observability]] · [[lecture-12-clean-state]] · [[ralph-playbook]]
