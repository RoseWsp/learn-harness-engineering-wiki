# Feature List

The foundational data structure of a harness. Not an optional memo — the backbone of scope control.

## What it is

A machine-readable list of features, each with behavior, verification command, and state. It replaces subjective "done" with verifiable status. ([[lecture-08-feature-lists]])

## The triple structure

Every feature has three parts:

1. **Behavior**: What it should do (observable, testable)
2. **Verification command**: How to prove it works (executable)
3. **State**: not_started / active / blocked / passing

## Pass-state gating

The agent cannot mark features as "passing." Only the harness — running verification — can make that transition. This prevents self-grading. ([[lecture-08-feature-lists]], [[lecture-09-premature-victory]])

## Minimal format

```json
{
  "id": "F001",
  "behavior": "User can create a document",
  "verification": "npm run test -- --grep 'create document'",
  "state": "passing",
  "evidence": "All 3 tests pass"
}
```

## Single source of truth

All scope information lives in one feature list. No duplicates across PROGRESS.md, Slack, and Jira. One list, one truth. ([[lecture-03-repo-as-system-of-record]])

## Granularity

Each feature should be completable in one session. If a feature takes multiple sessions, split it. ([[lecture-08-feature-lists]])

## WIP=1

Enforce working on one feature at a time. WIP limits are a Kanban principle that prevents agents from overreaching — starting 5 features and finishing none. ([[lecture-07-task-boundaries]])

## Case study

- **Memo mode** (unstructured notes): 20-minute state inference, rework from lost context
- **Backbone mode** (structured feature list): 3-minute state inference, zero rework ([[lecture-08-feature-lists]])

## See also

- [[wip-limit]] — why WIP=1 prevents overreach
- [[pass-state-gating]] — why only the harness marks features passing
- [[scope-surface]] — the DAG of task states
- [[harness-defined]] — feature lists as part of the State subsystem
