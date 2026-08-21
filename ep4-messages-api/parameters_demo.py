"""
Episode 4: How temperature and stop_sequences change Claude's output.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

def generate(prompt, temperature=1.0, stop=None):
    return client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=128,
        temperature=temperature,
        stop_sequences=stop or [],
        messages=[{"role": "user", "content": prompt}],
    ).content[0].text.strip()

if __name__ == "__main__":
    prompt = "List five creative names for a developer productivity app."
    print("=== temperature=0 (deterministic) ===\n", generate(prompt, temperature=0))
    print("\n=== temperature=1 (creative) ===\n",     generate(prompt, temperature=1))
    print("\n=== stop at '3.' ===\n",                 generate(prompt, stop=["3."]))
