# Scope Surface

A DAG of task states that makes project progress machine-readable and visible.

## What it is

The scope surface tracks every task's state: not_started → active → blocked → passing. It's a directed acyclic graph because tasks have dependencies — you can't test the export feature until the file system module is passing. ([[lecture-07-task-boundaries]])

## Why externalize it

Without an external scope surface, the agent holds task state in its context window. That state is fragile — it gets lost when context compacts, and it's invisible to the next session. Externalizing it into a file makes it durable and shareable. ([[lecture-05-continuity]])

## Relationship to feature lists

The [[feature-list]] is the concrete implementation of the scope surface. Each feature is a node in the DAG; the verification command is the gate for state transitions. ([[lecture-08-feature-lists]])

## See also

- [[feature-list]] — the data structure
- [[wip-limit]] — constraining how many nodes can be "active"
- [[lecture-07-task-boundaries]] — the full argument
