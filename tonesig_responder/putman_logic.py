import random

def generate_response(tonesig_code, tonesig_meta, d_field):
    label = tonesig_meta["label"]
    normalized_label = label.lower().strip()

    response_bank = {
        "double-bind sarcasm trap": [
            "That sounds like a trap disguised as a choice.",
            "That’s a classic bind — no real way to win there.",
            "It's hard to answer honestly when the frame’s dishonest."
        ],
        "escalated disappointment": [
            "That tone’s laced with pressure and judgment.",
            "You say you're not judging, but it’s hard to miss the weight behind that.",
            "Sounds like you want to help but are also getting tired."
        ],
        "guilt-layered urgency": [
            "There’s pressure here — not just to act, but to prove you care.",
            "Urgency and guilt — powerful tools when blended.",
            "Feels like emotional leverage more than a request."
        ],
        "reflective burden loop": [
            "I hear the loop — cycling through hope and fatigue.",
            "You’re naming the pattern, and that’s progress.",
            "We keep returning here — maybe that says something deeper."
        ],
        "symbolic emergence": [
            "That’s a breakthrough — you’re seeing meaning rise from the mess.",
            "Maybe this pressure wasn’t just about the task — it was pointing to something larger.",
            "You’re sensing the pattern beneath the conflict. That matters."
        ],
        "reflective calm": [
            "There’s quiet in this tone — like the pause between waves.",
            "You might be stepping outside the loop, finally seeing it whole.",
            "This feels like clarity after a storm. Not empty, but clear."
        ]
    }

    options = response_bank.get(normalized_label, [f"(ToneSig {tonesig_code}: {label})"])
    chosen = random.choice(options)
    return f"{chosen} (ToneSig {tonesig_code}: {label}, D-Field: {d_field})"