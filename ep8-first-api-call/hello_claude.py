"""
Episode 8: The absolute simplest Claude API call.
If this runs, you are ready to build anything.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello! Tell me one interesting fact about APIs."}],
)

print(response.content[0].text)
