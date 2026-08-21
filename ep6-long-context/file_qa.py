"""
Episode 6: Load any text file into Claude's context and ask questions.
Classic long-context document Q&A pattern.
"""
import sys
import anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

SYSTEM = (
    "You are a precise document analyst. "
    "Answer only from the provided document. "
    "If the answer is not in the document, say so clearly."
)

def file_qa(file_path, question):
    content = Path(file_path).read_text(encoding="utf-8")
    prompt  = f"<document>\n{content}\n</document>\n\nQuestion: {question}"
    return client.messages.create(
        model="claude-sonnet-4-6", max_tokens=512,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    ).content[0].text

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python file_qa.py <file_path> "<question>"')
        sys.exit(1)
    print(file_qa(sys.argv[1], sys.argv[2]))
