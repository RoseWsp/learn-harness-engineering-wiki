# Capability Gap

Benchmark performance doesn't predict real-world performance. The gap is where harness engineering lives.

## What it means

SWE-bench Verified top scores hover around 50-60%. That's on carefully selected tasks with clear descriptions and existing tests. In your daily dev environment — vague requirements, no tests, implicit rules — the number drops further. ([[lecture-01-capable-agents-still-fail]])

The gap between "what the model can do on a benchmark" and "what it actually does in your repo" is the capability gap. It's filled by the [[harness-defined|harness]], not by upgrading the model.

## The Anthropic experiment

Same model (Opus 4.5), same prompt ("build a 2D retro game maker"). Without harness: broken result in 20 minutes. With harness: fully playable game in 6 hours. The model didn't change. The harness closed the capability gap. ([[lecture-01-capable-agents-still-fail]])

## Don't reach for your wallet

When an agent fails, the instinct is "this model isn't good enough." Before upgrading, check the five harness subsystems: is the task specified? Are conventions visible? Is the environment clean? Is there verification? Is state persisted? Most failures are harness-induced, not model-induced. ([[lecture-01-capable-agents-still-fail]])

## See also

- [[harness-defined]] — what fills the capability gap
- [[overconfidence-bias]] — models overestimate their own accuracy
- [[lecture-01-capable-agents-still-fail]] — the full argument
