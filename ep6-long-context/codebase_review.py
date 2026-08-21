"""
Episode 6: Load multiple Python files and ask Claude to review the codebase.
Shows how to structure multi-file context with XML tags.
"""
import anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = (
    "You are a senior software engineer doing a code review. "
    "Identify bugs, security issues, and improvements. "
    "Reference specific file names in your feedback."
)

def review(file_paths):
    parts = [f'<file name="{p}">\n{Path(p).read_text()}\n</file>' for p in file_paths]
    prompt = "\n\n".join(parts) + "\n\nPlease review the codebase above."
    return client.messages.create(
        model="claude-sonnet-4-6", max_tokens=1024,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    ).content[0].text

if __name__ == "__main__":
    files = list(Path(".").glob("*.py"))
    if not files:
        print("No .py files found in current directory.")
    else:
        print(f"Reviewing {[str(f) for f in files]}\n")
        print(review([str(f) for f in files]))
