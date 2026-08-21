"""
Episode 1: Interactive CLI that recommends a Claude model
based on your use case.
"""

def recommend_model():
    print("\n=== Claude Model Selector ===\n")
    volume     = input("Expected requests/day? (low / medium / high): ").strip().lower()
    complexity = input("Task complexity?       (simple / moderate / complex): ").strip().lower()
    latency    = input("Latency sensitive?     (yes / no): ").strip().lower()

    if complexity == "complex":
        model  = "claude-opus-4-6"
        reason = "Complex reasoning tasks benefit from Opus's depth."
    elif volume == "high" or latency == "yes":
        model  = "claude-haiku-4-5"
        reason = "High volume or latency-sensitive work: Haiku for speed and cost."
    else:
        model  = "claude-sonnet-4-6"
        reason = "Balanced workload: Sonnet is the everyday sweet spot."

    print(f"\nRecommended: {model}")
    print(f"Reason     : {reason}")
    print(f'\nUse in code: model="{model}"')

if __name__ == "__main__":
    recommend_model()
