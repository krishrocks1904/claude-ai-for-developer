# Phase 1: Core Concepts of Claude AI

Companion code for the **Claude AI for Developers** YouTube series — Phase 1.

Each folder maps to one episode. Every episode has runnable code, a `.env.example`, and its own `README.md` with setup instructions and key concepts.

## Episodes

| # | Folder | Topic |
|---|--------|-------|
| 1 | `ep1-models-and-families` | Claude models, families, and how to choose |
| 2 | `ep2-tokens` | Tokens, context windows, and cost estimation |
| 3 | `ep3-pricing` | Pricing, rate limits, and cost calculator |
| 4 | `ep4-messages-api` | The Messages API — request/response structure |
| 5 | `ep5-system-prompts` | System prompts — giving Claude a brain |
| 6 | `ep6-long-context` | Long-context superpower — files and codebases |
| 7 | `ep7-safety-and-limits` | Claude's values, limits, and handling refusals |
| 8 | `ep8-first-api-call` | Capstone — CLI chatbot from scratch |

## Prerequisites

- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)

## Quick start

```bash
git clone https://github.com/YOUR_USERNAME/claude-ai-phase1.git
cd claude-ai-phase1
pip install anthropic python-dotenv
cp .env.example .env
# Add your API key to .env
```

Then `cd` into any episode folder and run its example:

```bash
cd ep1-models-and-families
python compare_models.py
```

## Series playlist

> Link to your YouTube playlist here

## License

MIT
