"""
Episode 1: Compare the same prompt across Claude model tiers.
Shows speed, response quality, and token usage side-by-side.
"""
import time
import anthropic
from dotenv import load_dotenv

load_dotenv(".env.local")
client = anthropic.Anthropic()

PROMPT = "Explain what a REST API is in 2 sentences, for a junior developer."

MODELS = [
    ("claude-haiku-4-5-20251001", "Haiku  (fast / cheap)"),
    ("claude-sonnet-4-6",         "Sonnet (balanced)    "),
    ("claude-opus-5",             "Opus   (powerful)    "),
]

def run_model(model_id, label):
    start = time.time()
    response = client.messages.create(
        model=model_id,
        max_tokens=256,
        messages=[{"role": "user", "content": PROMPT}],
    )
    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  Latency : {elapsed:.2f}s")
    print(f"  Tokens  : {response.usage.input_tokens} in / {response.usage.output_tokens} out")
    text = next(b.text for b in response.content if hasattr(b, "text"))
    print(f"  Response: {text.strip()}")

if __name__ == "__main__":
    print(f'Prompt: "{PROMPT}"\n')
    for model_id, label in MODELS:
        run_model(model_id, label)
    print(f"\n{'='*60}")
