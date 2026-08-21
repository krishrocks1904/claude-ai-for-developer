"""
Episode 4: A single Claude API call, fully annotated.
Every field of the response object is printed and explained.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=256,
    system="You are a helpful assistant that explains things clearly and concisely.",
    messages=[{"role": "user", "content": "What is a context window in an LLM?"}],
)

print("=== Response object fields ===")
print(f"id            : {response.id}")
print(f"model         : {response.model}")
print(f"stop_reason   : {response.stop_reason}")
print(f"input_tokens  : {response.usage.input_tokens}")
print(f"output_tokens : {response.usage.output_tokens}")
print(f"content type  : {response.content[0].type}")
print(f"\n=== Text ===")
print(response.content[0].text)
