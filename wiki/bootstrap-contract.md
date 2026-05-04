# Bootstrap Contract

Four conditions a new session must satisfy before feature work begins.

## The four conditions

1. **Can start the project from scratch** — `npm install && npm run dev` works
2. **Can run tests** — `npm run test` is green
3. **Can see current progress** — PROGRESS.md answers the question
4. **Can pick up next steps** — [[feature-list]] shows what's next

These are the output of the initialization phase. If any condition fails, don't start feature work — fix the foundation first. ([[lecture-06-initialization-phase]])

## Why separate initialization

When agents skip initialization and jump to coding, they build on shaky ground: missing deps, untested toolchains, implicit assumptions. The bootstrap contract ensures the foundation is solid before any feature work begins. ([[lecture-06-initialization-phase]])

## Warm start

Use project templates (create-react-app, fastapi-template) to preset infrastructure. The fastest way to satisfy the bootstrap contract is to start from a template that already satisfies it. ([[lecture-06-initialization-phase]])

## See also

- [[lecture-06-initialization-phase]] — the full argument
- [[cold-start-test]] — the five questions for any new session
- [[clean-state-checklist]] — the five conditions at session end
- [[init-sh]] — the initialization script
