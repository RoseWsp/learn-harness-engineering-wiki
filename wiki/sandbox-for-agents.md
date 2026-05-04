# Sandbox for Agents

**TL;DR** Autonomous agents need `--dangerously-skip-permissions`, which means the sandbox is your only security boundary. Don't run agents on bare metal — isolate them in containers or microVMs with minimum viable access.

## The security model

Ralph requires full autonomy to work. Asking for approval on every tool call breaks the loop. So you bypass the permission system entirely and rely on the sandbox for security.

Philosophy: **"It's not if it gets popped, it's when. And what is the blast radius?"**

Running without a sandbox exposes credentials, browser cookies, SSH keys, and access tokens on your machine. The blast radius is everything the user account can access.

## Principles

1. **Only the API keys and deploy keys needed for the task** — nothing extra
2. **No access to private data beyond requirements** — principle of least privilege
3. **Restrict network connectivity where possible** — whitelist only what's needed
4. **The sandbox is the security boundary** — inside, the agent has full permissions; outside, it has none

## Remote options

### E2B
Purpose-built for AI agents. Fastest cold start (~150ms Firecracker microVM). Pre-built Claude Code template. 200+ MCP tools via Docker partnership. 24-hour session limit on Pro. Best for production agent loops.

### Fly.io Sprites
Persistent environments that survive between executions. No time limits. Transactional snapshots (~300ms). Auto-sleep when idle. Best for long-running agents that need state across days.

### Modal
Python-optimized with gVisor isolation. Memory snapshots for fast cold starts. Scales to 10,000+ concurrent sandboxes. Best for Python ML/AI workloads.

### Cloudflare Sandboxes
Edge-native (330+ locations). Bindings model — zero network access by default. R2 FUSE for persistence. Still in beta. Best for edge apps already in Cloudflare ecosystem.

### Daytona
Sub-90ms cold start (container-based, faster than E2B's microVM). LangChain integration. Virtual desktops. Unlimited persistence. Young ecosystem.

## Local options

### Docker Sandboxes
`docker sandbox run claude` — instant local isolation. Credentials in persistent volume. `--dangerously-skip-permissions` enabled by default. Free, unlimited duration. Good for local dev and prototyping.

## Comparison

| | E2B | Sprites | Modal | Cloudflare |
|---|---|---|---|---|
| Cold start | ~150ms | <1s | 2-5s | 1-5s |
| Max duration | 24h (Pro) | Unlimited | 24h | Configurable |
| Isolation | Firecracker | Firecracker | gVisor | Container |
| Best for | Agent loops | Long-running agents | Python ML | Edge apps |

## Connection to harness principles

Sandboxing is part of the [[harness-defined|Environment subsystem]]. A broken environment (no sandbox, exposed credentials) undermines everything else. The [[clean-state-checklist]] implicitly assumes the environment is safe; without a sandbox, "clean state" includes "agent could have exfiltrated your secrets."

([[ralph-playbook]])
