"""
Episode 5: Same question answered with different system prompts.
Shows how dramatically system prompts shape Claude's behaviour.
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

QUESTION = "How should I handle errors in my code?"

PERSONAS = {
    "No system prompt": None,
    "Senior Java engineer": (
        "You are a senior Java engineer with 15 years of experience. "
        "Always answer with Java code using try-catch-finally. "
        "Be direct and opinionated. No unnecessary explanation."
    ),
    "Beginner-friendly tutor": (
        "You are a patient coding tutor for complete beginners. "
        "Use simple analogies, no jargon, and always encourage the learner. "
        "Keep answers under 80 words."
    ),
    "Technical doc writer": (
        "You are a technical documentation writer. Respond in structured markdown "
        "with a brief definition, a bullet list of best practices, and one code snippet."
    ),
}

def ask(system, question):
    kwargs = dict(model="claude-sonnet-4-6", max_tokens=256,
                  messages=[{"role": "user", "content": question}])
    if system:
        kwargs["system"] = system
    return client.messages.create(**kwargs).content[0].text

if __name__ == "__main__":
    for label, system in PERSONAS.items():
        print(f"\n{'='*60}\nPersona: {label}\n{'='*60}")
        print(ask(system, QUESTION))
