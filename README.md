# PUTMAN ToneSig™ Responder (Prototype)

This is a working proof-of-concept for a symbolic tone classification and response demo, based on the PUTMAN Model and Tone Vector System (TVS™).  
It simulates emotional tone recursion across a 5-turn scripted sequence, followed by a live conversation mode using ToneSig™ inputs.

## Features

- 🎭 Symbolic response system mapped to ToneSig codes like `¡13.83`
- 🔄 Recursive emotional memory across user turns
- 🧠 D-Field classification: D1–D4 (based on PUTMAN symbolic awareness states)
- 📊 Tone Memory Trail showing symbolic trace of user interaction

## Run the Demo

```bash
cd tonesig_responder
python3 -m tonesig_responder.main