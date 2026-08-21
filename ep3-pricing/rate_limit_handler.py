"""
Episode 3: Handle rate limit errors with exponential backoff.
Production-ready pattern for high-volume applications.
"""
import time
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

def call_with_retry(prompt, model="claude-haiku-4-5", max_retries=5):
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=256,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content[0].text
        except anthropic.RateLimitError:
            wait = 2 ** attempt
            print(f"Rate limited. Waiting {wait}s (attempt {attempt+1}/{max_retries})...")
            time.sleep(wait)
        except anthropic.APIStatusError as e:
            print(f"API error {e.status_code}: {e.message}")
            raise
    raise RuntimeError("Max retries exceeded.")

if __name__ == "__main__":
    result = call_with_retry("What is 2 + 2?")
    print(f"Response: {result}")
