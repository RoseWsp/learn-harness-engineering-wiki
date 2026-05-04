# Story Map → SLC Release

**TL;DR** Reframe "topics of concern" as activities (verbs in a user journey), sequence them into a story map, and slice horizontally into Simple/Lovable/Complete releases. Each slice is a coherent product, not a random bag of features.

## What it means

Geoff's Ralph workflow already aligns with Jobs-to-be-Done — breaking JTBDs into topics of concern, which become specs. But topics are capability-oriented ("color extraction system"). Activities are journey-oriented ("upload photo", "see extracted colors", "arrange layout").

Activities sequence naturally into a user flow, creating a **story map**: activities as columns (the journey backbone), capability depths as rows (the full space of what could be built).

```
UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

basic         auto           manual          export
bulk          palette        templates       collab
batch         AI themes      auto-layout     embed
```

Horizontal slices become candidate releases. Not every activity needs new capability in every release — some cells stay empty, as long as the slice is coherent.

## SLC over MVP

Jason Cohen's Simple/Lovable/Complete criteria:

- **Simple** — narrow scope you can ship fast
- **Complete** — fully accomplishes a job within that scope (not a broken preview)
- **Lovable** — people actually want to use it

MVPs optimize for learning at the customer's expense — "minimum" often means broken. SLC flips this: learn in-market while delivering real value. If it succeeds, you have optionality. If it fails, you still treated users well.

```
              UPLOAD    →   EXTRACT    →   ARRANGE     →   SHARE

Palette Picker:  basic         auto                           export
Mood Board:                    palette        manual
Design Studio:  batch         AI themes      templates       embed
```

- **Palette Picker** — Upload, extract, export. Instant value from day one.
- **Mood Board** — Adds arrangement. Creative expression enters the journey.
- **Design Studio** — Professional features.

## Operationalizing with Ralph

The default Ralph approach produces "whatever the specs describe" — it's capability-focused. To get SLC releases, ground activities in audience context:

```
Audience (who)
    └── has JTBDs (why)
            └── fulfilled by Activities (how)
```

**Phase 1** (Requirements): Define audience and JTBDs → `AUDIENCE_JTBD.md`. Then define activities → `specs/*.md`.

**Phase 2** (Planning): Updated prompt sequences activities into a journey map, determines the next SLC slice, and plans tasks for that slice only. Human verifies the slice before building.

**Phase 3** (Building): Standard building prompt against the scoped plan.

## Why AUDIENCE_JTBD.md as a separate file

- Single source of truth — prevents drift across specs
- Enables holistic reasoning: "What does this audience need MOST?"
- Referenced twice: during spec creation AND SLC planning
- Keeps activity specs focused on WHAT, not repeating WHO

## Connection to harness principles

Story mapping is [[progressive-disclosure]] at the product level: the full map shows what could be built, the current slice shows what should be built now. SLC slices enforce [[wip-limit|WIP limits]] at the release level — one coherent slice at a time. And the human verification step before building is a form of [[pass-state-gating]]: the plan doesn't pass until a human confirms it represents a valuable SLC release.

([[ralph-playbook]])
