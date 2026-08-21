# CLI Chatbot — Episode 8 Capstone

A full multi-turn Claude chatbot with streaming, cost tracking, and slash commands.

## Setup
```bash
pip install anthropic python-dotenv
cp ../../.env.example .env
# Paste your Anthropic API key into .env
python chatbot.py
```

## Slash commands
| Command  | What it does                |
|----------|-----------------------------|
| `/reset` | Clear conversation history  |
| `/cost`  | Show tokens used and cost   |
| `/quit`  | Exit and print session cost |
