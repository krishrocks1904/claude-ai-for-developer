"""
Episode 5: Use system prompts to lock in output format.
Produces JSON, markdown, and plain text from the same underlying question.
"""
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

QUESTION = "What are the top 3 Python web frameworks and their main use case?"

FORMATS = {
    "JSON": (
        "Respond ONLY with a valid JSON array. No markdown, no explanation. "
        'Each item: {"name": str, "use_case": str}'
    ),
    "Markdown table": "Respond with a markdown table only. Columns: Framework, Use case, Best for.",
    "Plain text":     "Respond in plain text only. One short paragraph. No markdown.",
}

def ask(system, question):
    return client.messages.create(
        model="claude-haiku-4-5", max_tokens=256,
        system=system,
        messages=[{"role": "user", "content": question}],
    ).content[0].text.strip()

if __name__ == "__main__":
    for fmt, system in FORMATS.items():
        print(f"\n=== {fmt} ===")
        result = ask(system, QUESTION)
        print(result)
        if fmt == "JSON":
            try:
                print(f"\nParsed: {json.loads(result)}")
            except json.JSONDecodeError as e:
                print(f"JSON parse error: {e}")
