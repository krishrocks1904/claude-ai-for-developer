"""
Episode 7: A production-safe Claude wrapper.
Handles refusals, rate limits, and API errors with consistent fallback.
"""
import anthropic
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

REFUSAL_PHRASES = ["i can't", "i cannot", "i'm not able", "i won't", "i must decline"]

@dataclass
class ClaudeResult:
    text: str
    is_refusal: bool
    error: str | None = None

def safe_call(prompt, system="", model="claude-haiku-4-5", max_tokens=512,
              fallback="Sorry, I couldn't process that request."):
    try:
        kwargs = dict(model=model, max_tokens=max_tokens,
                      messages=[{"role": "user", "content": prompt}])
        if system:
            kwargs["system"] = system
        r = client.messages.create(**kwargs)
        text = r.content[0].text
        return ClaudeResult(text=text, is_refusal=any(p in text.lower() for p in REFUSAL_PHRASES))
    except anthropic.RateLimitError:
        return ClaudeResult(text=fallback, is_refusal=False, error="rate_limit")
    except anthropic.APIStatusError as e:
        return ClaudeResult(text=fallback, is_refusal=False, error=f"api_{e.status_code}")
    except Exception as e:
        return ClaudeResult(text=fallback, is_refusal=False, error=str(e))

if __name__ == "__main__":
    result = safe_call("Explain what an API key is.", system="You are a helpful tutor.")
    print(f"Response   : {result.text}")
    print(f"Is refusal : {result.is_refusal}")
    print(f"Error      : {result.error}")
