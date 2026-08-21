"""
Episode 7: Detect Claude refusals and handle them gracefully.
In production you need to distinguish a refusal from a normal response.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

REFUSAL_PHRASES = [
    "i can't", "i cannot", "i'm not able", "i won't",
    "i'm unable", "i must decline", "i don't feel comfortable",
]

def call_claude(prompt):
    r = client.messages.create(
        model="claude-haiku-4-5", max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )
    text = r.content[0].text
    is_refusal = any(p in text.lower() for p in REFUSAL_PHRASES)
    return {"text": text, "is_refusal": is_refusal}

if __name__ == "__main__":
    prompts = [
        ("Normal", "What is a Python generator?"),
        ("Creative fiction", "Write a short story about a hacker learning ethics."),
    ]
    for label, prompt in prompts:
        result = call_claude(prompt)
        status = "REFUSAL" if result["is_refusal"] else "OK"
        print(f"\n[{status}] {label}: {prompt[:60]}")
        print(f"Reply: {result['text'][:200]}...")
