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

## Which model should I use?

The profile ships with `z-ai/glm-5.2` via Nous Portal, but you can swap to any model that Hermes supports. For this aim-coaching agent, you need a model that can **follow structured instructions, use tools (web search), and produce structured output** — but you don't need a top-tier reasoning model. Here are the best free and low-cost options:

### Option A — Nous Portal (free models, zero setup beyond `hermes setup`)

These are included with a Nous Portal account at no extra cost. Just run `hermes setup`, pick Nous, and select one of these:

| Model | Portal Price | Context | Why it works here |
|---|---|---|---|
| `inclusionai/ling-3.1-flash` | **FREE** | 262K | Strong general reasoning + tool use. Best free Portal pick for this agent. |
| `inclusionai/ling-3.0-flash-sante` | **FREE** | 262K | Slightly older but capable. Good fallback. |
| `meituan/longcat-2.5-preview` | **FREE** | — | Solid text model, handles structured output well. |
| `poolside/laguna-s-2.1` | **FREE** | 262K | Coding-focused but handles agentic tool calls fine. |
| `poolside/laguna-xs-2.1` | **FREE** | 262K | Lighter variant of Laguna S. |
| `stepfun/step-3.7-flash` | **FREE** | — | Fast, capable. Good for quick diagnosis turns. |
| `upstage/solar-mini-4` | **FREE** | — | Small and efficient for straightforward tasks. |

**Recommended:** `inclusionai/ling-3.1-flash` — it's free on Portal, has 262K context (plenty for the SOUL prompt + your notes), and handles tool calling well.

### Option B — Google Gemini (free API tier)

Google offers a free API tier for Gemini Flash models. Sign up at [ai.google.dev](https://ai.google.dev), get an API key, and set it in your `.env`:

```bash
# .env
GOOGLE_API_KEY=your_key_here
```

| Model | Price | Context | Rate Limit | Notes |
|---|---|---|---|---|
| `gemini-3.8-flash` | **FREE** (free tier) | 1M | ~20 req/day | Newest Flash. Excellent for tool use. |
| `gemini-3.7-flash` | **FREE** (free tier) | 1M | ~20 req/day | Previous gen, still very capable. |
| `gemini-3.6-flash` | **FREE** (free tier) | 1M | ~20 req/day | Older but stable. |

**Caveat:** The free tier is limited to ~20 requests/day, which is enough for 1–2 aim diagnoses per day but not heavy use.

To switch, run:
```bash
hermes config set model.default gemini-3.8-flash
hermes config set model.provider gemini
```

### Option C — OpenRouter (free models, $10 one-time unlocks higher limits)

Create an account at [openrouter.ai](https://openrouter.ai), add $10 in credits (one-time), and you get 1,000 requests/day on free models instead of 50/day.

```bash
# .env
OPENROUTER_API_KEY=your_key_here
```

| Model | Price | Context | Notes |
|---|---|---|---|
| `nvidia/nemotron-3-ultra-550b-a55b:free` | **$0** | 1M | 550B MoE, 55B active. Strongest free model on OpenRouter. |
| `nvidia/nemotron-3.5-lightning:free` | **$0** | 1M | 30B MoE, 3B active. Fast and capable. |
| `nvidia/nemotron-3-super-120b-a12b:free` | **$0** | 262K | Good balance of speed and quality. |
| `poolside/laguna-s-2.1:free` | **$0** | 262K | Coding agent but handles tool calls well. |
| `qwen/qwen3.8-27b:free` | **$0** | 262K | Solid general-purpose model. |

**Recommended:** `nvidia/nemotron-3-ultra-550b-a55b:free` — best quality free model, 1M context, generous rate limits.

To switch:
```bash
hermes config set model.default nvidia/nemotron-3-ultra-550b-a55b:free
hermes config set model.provider openrouter
```

### Option D — DeepSeek (cheapest paid, high quality)

DeepSeek doesn't have a free tier but is extremely cheap — pennies per session for this use case.

```bash
# .env
DEEPSEEK_API_KEY=your_key_here
```

| Model | Input (cache hit) | Input (cache miss) | Output | Notes |
|---|---|---|---|---|
| `deepseek-chat` | $0.003/1M | $0.15/1M | $0.28/1M | Best value. A full diagnosis session costs ~$0.001. |
| `deepseek-reasoner` | $0.003/1M | $0.15/1M | $0.28/1M | Adds reasoning steps. Good for complex diagnoses. |

To switch:
```bash
hermes config set model.default deepseek-chat
hermes config set model.provider deepseek
```

### Quick recommendation

| Your situation | Use this |
|---|---|
| **Zero budget, no signup hassle** | Nous Portal → `inclusionai/ling-3.1-flash` (free) |
| **Zero budget, already have Google account** | Google Gemini → `gemini-3.8-flash` (free tier, ~20 req/day) |
| **$10 one-time, want best free quality** | OpenRouter → `nvidia/nemotron-3-ultra-550b-a55b:free` |
| **Cheapest paid, best reliability** | DeepSeek → `deepseek-chat` (~$0.001 per session) |
| **Just want it to work, don't care about cost** | Keep the default `z-ai/glm-5.2` via Nous Portal |

## Customization

After install, you can freely customize without affecting updates:
- Edit `SOUL.md` to tweak the diagnostic engine or add new Viscose classes
- Edit `config.yaml` to change model, provider, or toolsets (see model switching commands above)
- Add or remove skills in `skills/`
- Hermes will preserve your local changes through `hermes profile update` (it stashes non-conflicting local edits)

## License

MIT — see `LICENSE` file if included, or treat as MIT by default.
