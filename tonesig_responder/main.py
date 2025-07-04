# tonesig_responder/main.py

from tonesig_responder.simulate_inputs import test_inputs
from tonesig_responder.tonesig_data import get_tonesig_metadata
from tonesig_responder.putman_logic import generate_response
from collections import Counter

def run_tonesig_demo():
    print("\n===== 🎭 Multi-Turn PUTMAN ToneSig™ Demo =====\n")

    for i, entry in enumerate(test_inputs, start=1):
        tonesig = entry["tonesig"]
        metadata = get_tonesig_metadata(tonesig)
        label = metadata["label"]
        description = metadata["description"]
        d_field = entry["d_field"]
        message = entry["message"]

        print(f"=== Turn {i} ===")
        print(f"🧠 ToneSig: {tonesig} → {label}")
        print(f"📘 Description: {description}")
        print(f"🧭 D-Field: {d_field}")
        print(f"🗨️ Message: {message}")
        print("-" * 60)

        tonesig_meta = {
            "label": label,
            "description": description
        }

        response = generate_response(tonesig, tonesig_meta, d_field)
        print(f"🤖 Response:\n{response}")
        print("\n" + "=" * 60 + "\n")

    print("✅ Demo complete. You just ran a symbolic tone recursion test across emotional beats.")


def live_conversation():
    print("\n🟢 Enter live messages to simulate conversation. Type 'exit' to quit.\n")
    memory_trail = []

    while True:
        user_input = input("🗨️ You: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        # Simple tone matching logic
        if "blame" in user_input or "pressure" in user_input:
            tonesig_code = "¡13.83"
            label = "double-bind sarcasm trap"
            description = "Passive-aggressive framing disguised as choice."
            d_field = "D2"

        elif "my fault" in user_input or "sorry" in user_input:
            tonesig_code = "¡28.12"
            label = "guilt-layered urgency"
            description = "Urgency amplified by moral obligation."
            d_field = "D2"

        elif "pattern" in user_input or "cycle" in user_input:
            tonesig_code = "¡31.76"
            label = "reflective burden loop"
            description = "Tension masked by vulnerability."
            d_field = "D3"

        elif "see now" in user_input or "not just about" in user_input:
            tonesig_code = "¡33.91"
            label = "symbolic emergence"
            description = "Breakthrough insight about a deeper pattern."
            d_field = "D4"

        elif "hate" in user_input or "awful" in user_input:
            tonesig_code = "¡21.00"
            label = "emotional fracture"
            description = "Tone carrying inner fracture or rejection."
            d_field = "D2"

        else:
            tonesig_code = "¡42.00"
            label = "reflective calm"
            description = "A settled awareness after emotional intensity."
            d_field = "D3"

        tonesig_meta = {
            "label": label,
            "description": description
        }

        response = generate_response(tonesig_code, tonesig_meta, d_field)
        print(f"\n🤖 [¡{tonesig_code} / {label}]: {response}")

        memory_trail.append(f"¡{tonesig_code} — {label}")
        print("\n📈 Tone Memory Trail:")
        for i, entry in enumerate(memory_trail, start=1):
            print(f"  [{i}] {entry}")
        print()


if __name__ == "__main__":
    run_tonesig_demo()
    live_conversation()