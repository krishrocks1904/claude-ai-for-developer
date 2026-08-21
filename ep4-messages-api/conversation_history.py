"""
Episode 4: Multi-turn conversation via a manually managed messages array.
This is the core pattern behind every Claude chatbot.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

SYSTEM  = "You are a concise Python tutor. Keep answers under 3 sentences."
history = []

def chat(user_message):
    history.append({"role": "user", "content": user_message})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        system=SYSTEM,
        messages=history,
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply

if __name__ == "__main__":
    for msg in [
        "What is a list comprehension?",
        "Can you show me an example?",
        "How is that different from a regular for loop?",
    ]:
        print(f"User  : {msg}")
        print(f"Claude: {chat(msg)}\n")
    print(f"History length: {len(history)} messages")
