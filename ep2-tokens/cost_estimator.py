"""
Episode 2: Estimate API costs before sending requests.
Plug in your expected usage to forecast monthly spend.
"""

PRICING = {
    "claude-haiku-4-5":  {"input": 0.80,  "output": 4.00},
    "claude-sonnet-4-6": {"input": 3.00,  "output": 15.00},
    "claude-opus-4-6":   {"input": 15.00, "output": 75.00},
}

def estimate(model, avg_input_tokens, avg_output_tokens, requests_per_day):
    p = PRICING[model]
    daily = (avg_input_tokens * requests_per_day / 1_000_000 * p["input"] +
             avg_output_tokens * requests_per_day / 1_000_000 * p["output"])
    print(f"\nModel           : {model}")
    print(f"Requests/day    : {requests_per_day:,}")
    print(f"Avg tokens/req  : {avg_input_tokens} in / {avg_output_tokens} out")
    print(f"Daily cost      : ${daily:.4f}")
    print(f"Monthly estimate: ${daily * 30:.2f}")

if __name__ == "__main__":
    print("=== Cost Estimator ===")
    estimate("claude-sonnet-4-6", 500, 300, 1_000)
    estimate("claude-haiku-4-5",  200, 50,  50_000)
