"""
Episode 3: Track token usage and estimated cost across multiple calls.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

PRICING = {
    "claude-haiku-4-5":  {"input": 0.80, "output": 4.00},
    "claude-sonnet-4-6": {"input": 3.00, "output": 15.00},
}

class UsageTracker:
    def __init__(self, model):
        self.model = model
        self.input_tokens = 0
        self.output_tokens = 0
        self.calls = 0

    def ask(self, prompt):
        r = client.messages.create(
            model=self.model, max_tokens=128,
            messages=[{"role": "user", "content": prompt}],
        )
        self.input_tokens  += r.usage.input_tokens
        self.output_tokens += r.usage.output_tokens
        self.calls += 1
        return r.content[0].text

    def report(self):
        p = PRICING.get(self.model, {"input": 0, "output": 0})
        cost = (self.input_tokens  / 1_000_000 * p["input"] +
                self.output_tokens / 1_000_000 * p["output"])
        print(f"\n=== Usage Report ===")
        print(f"Calls         : {self.calls}")
        print(f"Input tokens  : {self.input_tokens:,}")
        print(f"Output tokens : {self.output_tokens:,}")
        print(f"Est. cost     : ${cost:.6f}")

if __name__ == "__main__":
    tracker = UsageTracker("claude-haiku-4-5")
    for q in ["What is Python?", "Name 3 web frameworks.", "What is a REST API?"]:
        print(f"Q: {q}\nA: {tracker.ask(q)}\n")
    tracker.report()
