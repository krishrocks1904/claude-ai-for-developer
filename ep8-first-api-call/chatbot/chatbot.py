"""
Episode 8 capstone: Multi-turn CLI chatbot with:
  - Streaming output (text appears as it is generated)
  - Conversation history
  - Token and cost tracking
  - Slash commands: /reset  /cost  /quit
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

MODEL   = "claude-sonnet-4-6"
PRICING = {"input": 3.00, "output": 15.00}  # per million tokens

SYSTEM = (
    "You are a helpful, concise developer assistant. "
    "You specialise in Python, APIs, and software engineering. "
    "Keep answers focused and practical."
)

history       = []
total_input   = 0
total_output  = 0

def cost():
    return (total_input  / 1_000_000 * PRICING["input"] +
            total_output / 1_000_000 * PRICING["output"])

def stream_reply(user_input):
    global total_input, total_output
    history.append({"role": "user", "content": user_input})
    full = ""
    print("\nClaude: ", end="", flush=True)
    with client.messages.stream(
        model=MODEL, max_tokens=1024, system=SYSTEM, messages=history
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
            full += chunk
        final = stream.get_final_message()
        total_input  += final.usage.input_tokens
        total_output += final.usage.output_tokens
    print("\n")
    history.append({"role": "assistant", "content": full})

def handle_command(cmd):
    global history
    if cmd == "/quit":
        print(f"Session cost: ${cost():.6f}. Goodbye!")
        return False
    if cmd == "/reset":
        history = []
        print("History cleared.\n")
    if cmd == "/cost":
        print(f"Tokens: {total_input} in / {total_output} out | Cost: ${cost():.6f}\n")
    return True

if __name__ == "__main__":
    print("Claude CLI Chatbot  |  /reset  /cost  /quit\n")
    running = True
    while running:
        try:
            msg = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not msg:
            continue
        running = handle_command(msg) if msg.startswith("/") else (stream_reply(msg) or True)
