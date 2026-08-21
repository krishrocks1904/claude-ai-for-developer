"""
Episode 2: Count tokens in different types of content
using the Anthropic count_tokens API.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-haiku-4-5"

SAMPLES = {
    "Plain English": "The quick brown fox jumps over the lazy dog. " * 10,
    "Python code": """
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]
""" * 5,
    "JSON payload": '{"user_id": 123, "action": "login", "timestamp": "2025-01-01T00:00:00Z"}' * 10,
}

def count_tokens(text):
    r = client.messages.count_tokens(
        model=MODEL,
        messages=[{"role": "user", "content": text}],
    )
    return r.input_tokens

if __name__ == "__main__":
    print(f"{'Content type':<20} {'Words':>8} {'Tokens':>8} {'Ratio':>8}")
    print("-" * 48)
    for label, text in SAMPLES.items():
        words  = len(text.split())
        tokens = count_tokens(text)
        print(f"{label:<20} {words:>8} {tokens:>8} {tokens/words:>8.2f}")

    print("\nContext window: 200,000 tokens (all current Claude models)")
