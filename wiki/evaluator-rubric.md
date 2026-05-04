# Evaluator Rubric

A structured quality scoring framework. Turns subjective "looks good" into quantifiable metrics.

## What it scores

Typical dimensions:

- **Code correctness**: Does it do what was asked?
- **Architecture compliance**: Does it follow the project's patterns?
- **Test coverage**: Are the important paths tested?
- **Clean state**: Does it leave the project in a [[clean-state-checklist|clean state]]?

Each dimension gets a score. The overall score determines whether the task passes. ([[lecture-11-observability]])

## Why structure matters

Without a rubric, evaluation is subjective. "Looks good" means different things to different evaluators. A rubric makes evaluation consistent and repeatable — essential when the evaluator is a separate agent from the generator. ([[lecture-09-premature-victory]])

## The three-agent pattern

- **Planner**: Breaks the task into steps
- **Generator**: Implements the steps
- **Evaluator**: Scores the output against the rubric

This is the architecture from Anthropic's experiment: same model, but with evaluation as a separate, independent step. ([[lecture-09-premature-victory]])

## See also

- [[sprint-contract]] — the pre-task agreement that rubrics reference
- [[three-layer-termination]] — the verification gates
- [[lecture-11-observability]] — process observability
- [[lecture-09-premature-victory]] — the three-agent pattern
