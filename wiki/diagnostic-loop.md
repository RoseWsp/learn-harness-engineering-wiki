# Diagnostic Loop

Execute → observe failure → attribute to layer → fix → re-execute. The systematic debugging process for agent failures.

## What it means

When an agent fails, don't blame the model. Attribute the failure to one of five layers:

1. **Task specification** — was the task clearly defined?
2. **Context** — did the agent have the right information?
3. **Environment** — were deps, versions, and services correct?
4. **Verification** — could the agent check its own work?
5. **State** — was progress from previous sessions available?

Fix the layer, re-execute, measure the improvement. Repeat until reliability is acceptable. ([[lecture-01-capable-agents-still-fail]])

## Why layer attribution matters

Most people's instinct is "the model isn't good enough." But most failures are harness-induced — the model is capable but the environment is defective. The diagnostic loop forces you to find and fix the actual layer, not throw a bigger model at the problem. ([[lecture-01-capable-agents-still-fail]])

## Isometric model control

Remove one subsystem at a time to measure its impact. This is how you quantify the ROI of each harness component. ([[lecture-02-what-harness-actually-is]])

## See also

- [[harness-defined]] — the five subsystems that the diagnostic loop tests
- [[capability-gap]] — why the gap exists
- [[ralph-loop]] — the Ralph loop as an instance of the diagnostic loop: each iteration is a discrete experiment
- [[lecture-01-capable-agents-still-fail]] — the full argument
