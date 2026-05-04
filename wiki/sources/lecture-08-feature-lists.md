---
type: lecture
date: 2025-04-29
author: WalkingLabs
url: https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/
raw: raw/docs/en/lectures/lecture-08-why-feature-lists-are-harness-primitives/index.md
---

# Lecture 08. Feature Lists Are Harness Primitives

Feature lists are foundational data structures, not optional memos. They constrain what the agent does.

## What it means

Agents use their own "done" criteria (code looks complete), which differs from user expectations. Unstructured progress notes cause rework and long session startup times. A feature list replaces subjective "done" with machine-verifiable state.

## The triple structure

Each feature has three parts:

1. **Behavior**: What it should do (observable, testable)
2. **Verification command**: How to prove it works (executable)
3. **State**: not_started / active / blocked / passing — only the harness can mark "passing"

## Pass-state gating

The agent cannot directly mark features as "passing." Only the harness — running verification — can transition a feature to the passing state. This prevents the agent from grading its own homework.

## Single source of truth

All scope information must come from one feature list. No duplicates in PROGRESS.md, Slack, and a Jira board. One list, one truth.

## Minimal feature list format

```json
{
  "id": "F001",
  "behavior": "User can create a document",
  "verification": "npm run test -- --grep 'create document'",
  "state": "passing",
  "evidence": "All 3 tests pass"
}
```

## Case study

- **Memo Mode**: Unstructured notes, 20-minute state inference, re-implementation of features
- **Backbone Mode**: Structured feature list, 3-minute state inference, zero rework

## See also

- [[lecture-07-task-boundaries]] — why WIP=1 and scope surfaces matter
- [[lecture-09-premature-victory]] — preventing false completions
- [[feature-list]] — the data structure in detail
- [[pass-state-gating]] — why only the harness marks features passing
