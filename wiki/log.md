# Log

## [2026-05-04 22:30] ingest | Learn Harness Engineering course (12 lectures)

Ingested the full Learn Harness Engineering course from WalkingLabs (raw/ directory). Created source-summary pages for all 12 lectures, plus 18 concept/entity pages covering core harness engineering themes. Built home.md with SVG concept map, index.md, and log.md.

**Pages created:**
- Sources: lecture-01 through lecture-12 (12 pages)
- Concepts: harness-defined, agents-md, feature-list, progressive-disclosure, wip-limit, pass-state-gating, three-layer-termination, capability-gap, overconfidence-bias, lost-in-middle-effect, context-anxiety, harness-rot, diagnostic-loop, progress-md, cold-start-test, clean-state-checklist, bootstrap-contract, init-sh, scope-surface, sprint-contract, evaluator-rubric, e2e-vs-unit-testing, quality-document (23 pages)
- Structural: home.md, index.md, log.md (3 pages)

**Cross-links:** Every page links out to related concepts and back to its source lecture. home.md links to all 12 source pages. index.md catalogs all 38 pages.

## [2026-05-04 23:15] ingest | The Ralph Playbook (Clayton Farr)

Ingested the Ralph Playbook from `raw/how-to-ralph-wiggum/` — Clayton Farr's detailed operational guide to the Ralph pattern (Geoffrey Huntley's loop-based autonomous coding approach). Created 1 source-summary page and 6 concept pages.

**Pages created:**
- Source: ralph-playbook
- Concepts: ralph-loop, subagent-scheduling, backpressure-signals, sandbox-for-agents, acceptance-driven-backpressure, story-map-slc

**Cross-links added to existing pages:**
- harness-defined → ralph-loop, backpressure-signals, sandbox-for-agents
- agents-md → ralph-loop (new section on Ralph's AGENTS.md role)
- wip-limit → ralph-loop, story-map-slc
- pass-state-gating → acceptance-driven-backpressure, ralph-loop
- three-layer-termination → backpressure-signals, ralph-loop
- progressive-disclosure → subagent-scheduling
- diagnostic-loop → ralph-loop
- e2e-vs-unit-testing → backpressure-signals, acceptance-driven-backpressure
- context-anxiety → ralph-loop, subagent-scheduling
- overconfidence-bias → backpressure-signals, acceptance-driven-backpressure

## [2026-05-05 10:00] create | Harness 刻意训练指南

Created [[harness-deliberate-practice]] — a 6-week progressive training guide for developers to build harness engineering skills through deliberate practice. Covers AGENTS.md writing, test backpressure, state persistence, WIP=1 scope control, Ralph loop operation, and ablation experiments. Updated index.md and home.md with cross-links.

## [2026-05-05 11:30] ingest + create | SkipLabs Lights-Out Challenge

Ingested two SkipLabs articles (Hugo Venturini) that challenge the current harness model's assumption that humans remain in the loop. Created source-summary pages and three concept pages analyzing the implications.

**Source pages created:**
- skiplabs-codegen-as-compiler — Treat agent output like compiler output
- skiplabs-future-of-tools — Code was never for machines — until now

**Concept pages created:**
- codegen-as-compiler-output — Compiler analogy: trust the process, not the artifact
- agent-native-tooling — Tools will bifurcate for humans vs agents
- lights-out-challenge — The endgame: harness as trust infrastructure that makes human presence unnecessary

**Cross-links added:**
- home.md → lights-out challenge section with three implications
- agents-md → codegen-as-compiler-output (formal spec as next step)
- backpressure-signals → codegen-as-compiler-output (AI-checks-AI as first-class CI)
- harness-deliberate-practice → lights-out-challenge (code judgment long-term positioning)
