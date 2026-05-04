# Cold-Start Test

Five questions a fresh agent session should be able to answer. If it can't, your knowledge is scattered.

## The five questions

1. What does this project do?
2. How do I run it?
3. How do I test it?
4. What's the current state of work?
5. Where do I find X?

If a brand new session (no prior context) can't answer these from the repo alone, the knowledge is not in the repo. And if it's not in the repo, it doesn't exist for the agent. ([[lecture-03-repo-as-system-of-record]])

## Why it matters

When the Cold-Start Test fails, agents burn their context budget on discovery — just finding information before any real work starts. This is **discovery cost**, and it should be near zero.

## How to pass

- [[agents-md]] answers questions 1-3 (overview, run, test)
- [[progress-md]] answers question 4 (current state)
- ARCHITECTURE.md per module answers question 5 (where to find X)

## See also

- [[lecture-03-repo-as-system-of-record]] — the full argument
- [[agents-md]] — the landing page that answers most cold-start questions
- [[harness-defined]] — cold-start as a property of the Instructions + State subsystems
