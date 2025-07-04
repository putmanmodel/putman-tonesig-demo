def get_tonesig_metadata(tonesig_code):
    # For demo purposes, hardcode matching examples
    sample_metadata = {
        "¡13.83": {"label": "double-bind sarcasm trap", "description": "Passive-aggressive framing disguised as choice."},
        "¡17.45": {"label": "escalated disappointment", "description": "Subtle judgment veiled as concern."},
        "¡28.12": {"label": "guilt-layered urgency", "description": "Urgency amplified by moral obligation."},
        "¡31.76": {"label": "reflective burden loop", "description": "Tension masked by vulnerability."},
        "¡33.91": {"label": "symbolic emergence", "description": "Breakthrough insight about a deeper pattern."},
    }

    return sample_metadata.get(tonesig_code, {"label": "unknown tone", "description": ""})

tonesig_metadata = {
    "¡13.83": {
        "label": "double-bind sarcasm trap",
        "description": "Passive-aggressive framing disguised as choice."
    },
    "¡17.45": {
        "label": "escalated disappointment",
        "description": "Subtle judgment veiled as concern."
    },
    "¡28.12": {
        "label": "guilt-layered urgency",
        "description": "Urgency amplified by moral obligation."
    },
    "¡31.76": {
        "label": "reflective burden loop",
        "description": "Tension masked by vulnerability."
    },
    "¡33.91": {
        "label": "symbolic emergence",
        "description": "Breakthrough insight about a deeper pattern."
    },
    "¡42.00": {
        "label": "reflective calm",
        "description": "A settled awareness after emotional intensity."
    },
    "¡21.00": {
        "label": "emotional fracture",
        "description": "A break in affective coherence or stability."
    }
}

def get_tonesig_metadata(tonesig_code):
    return tonesig_metadata.get(tonesig_code, {
        "label": "unknown tone",
        "description": ""
    })