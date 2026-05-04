# Lost in the Middle Effect

Content in the middle of long contexts is 30-40% less effective. This is why 600-line instruction files fail.

## What it means

Liu et al. (2023) showed that LLMs struggle with information in the middle of long contexts. The beginning and end are well-attended; the middle is a dead zone. Rules buried in line 400 of a 600-line AGENTS.md are essentially invisible to the agent. ([[lecture-04-giant-instruction-file-fails]])

## The fix

[[progressive-disclosure]]: Keep AGENTS.md short (50-200 lines) and link to topic-specific docs. Each doc is short enough that the middle doesn't exist — everything is effectively at the beginning or end.

## Case study

600-line monolithic AGENTS.md → 80-line routing + 3 topic docs → success rate 45% → 72%. The same rules, restructured to avoid the middle dead zone. ([[lecture-04-giant-instruction-file-fails]])

## See also

- [[progressive-disclosure]] — the structural fix
- [[agents-md]] — how to keep the routing file short
- [[lecture-04-giant-instruction-file-fails]] — the full argument
