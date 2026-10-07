# Aim Coach — Motor Learning & Aim Diagnostics AI

A Hermes Agent profile that turns aim-coaching notes, VOD reviews, and player feedback into evidence-based motor diagnoses and sustainable weekly KovaaK's practice plans.

## What's inside

| Component | Description |
|---|---|
| **SOUL.md** | System prompt: the Viscose Benchmark & Kinetic Chain diagnostic engine, KovaaK's live search rules, 1-skill-per-day weekly rotation, progression gates, and edge-case guardrails |
| **config.yaml** | Model (`z-ai/glm-5.2` via Nous), toolsets, compression, memory, TTS/STT, and platform routing |
| **skills/gaming/aim-coaching** | Aim diagnosis skill — matches drills to movement geometry, verifies scenarios in KovaaK's database |
| **skills/gaming/kovaaks-playlist-builder** | Generates and validates KovaaK's playlist JSON files |
| **~60 bundled skills** | Full Hermes skill catalog (creative, productivity, research, software-development, media, etc.) |

## Prerequisites

1. **Install Hermes Agent** (if you don't have it already):
   ```bash
   # macOS / Linux / WSL2
   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

   # Windows — download the desktop bundle or see the Windows native guide
   # https://hermes-agent.nousresearch.com/docs/getting-started/installation
   ```

2. **Authenticate with Nous Portal** (or any supported provider):
   ```bash
   hermes setup
   ```
   Follow the interactive prompts to pick a model and sign in. This agent uses `z-ai/glm-5.2` via the Nous provider.

## Install this profile

```bash
hermes profile install github.com/VendettaTheGreat/aim-coach
```

That's it. The installer will:
- Download the full profile (SOUL, config, skills, cron)
- Create a `.env.EXAMPLE` from the manifest — copy it to `.env` and fill in any optional keys you need
- Skip all secrets, memories, sessions, and caches (those stay local to each user)

## Run it

```bash
# Start chatting in the CLI
aim-coach chat

# Or launch the desktop app
hermes desktop
```

Then just paste in your aim-coaching notes, VOD observations, or player feedback and ask for a diagnosis + weekly plan.

## Update to the latest version

When Gabriel pushes new scenarios, skill updates, or config changes:

```bash
hermes profile update aim-coach
```

Your own memories, sessions, and API keys are preserved — only the distribution content (SOUL, config, skills) is updated.

## What's NOT included (and why)

| Excluded | Reason |
|---|---|
| `.env`, `auth.json` | Secrets — each user brings their own credentials |
| `memories/`, `sessions/` | Personal conversation history |
| `state.db`, `logs/` | Runtime databases and logs |
| `assets/avatar.png` | Personal avatar (optional — add your own) |

## Customization

After install, you can freely customize without affecting updates:
- Edit `SOUL.md` to tweak the diagnostic engine or add new Viscose classes
- Edit `config.yaml` to change model, provider, or toolsets
- Add or remove skills in `skills/`
- Hermes will preserve your local changes through `hermes profile update` (it stashes non-conflicting local edits)

## License

MIT — see `LICENSE` file if included, or treat as MIT by default.
