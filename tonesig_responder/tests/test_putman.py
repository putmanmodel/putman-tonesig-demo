import pytest
import re

from tonesig_responder.putman_logic import generate_response
from tonesig_responder.tonesig_data import get_tonesig_metadata
from tonesig_responder.simulate_inputs import test_inputs

@pytest.mark.parametrize("entry", test_inputs)
def test_generate_response_contains_metadata(entry):
    code = entry["tonesig"]
    meta = {"label": entry["label"], "description": entry["description"]}
    d_field = entry["d_field"]
    response = generate_response(code, meta, d_field)

    # Must mention the label and D-Field
    assert entry["label"] in response
    assert f"D-Field: {d_field}" in response

    # ToneSig code formatted correctly
    assert f"ToneSig {code}" in response

@pytest.mark.parametrize("unknown_code", ["¡99.99", "X42"])
def test_fallback_for_unknown_tonesig(unknown_code):
    meta = get_tonesig_metadata(unknown_code)
    # Should get the 'unknown tone' label
    assert meta["label"] == "unknown tone"
    # And generate_response uses fallback list
    response = generate_response(unknown_code, meta, "D0")
    assert f"ToneSig {unknown_code}" in response

def test_run_demo_no_exception(capfd):
    # import here to avoid side-effects on module load
    from tonesig_responder.main import run_tonesig_demo
    # Should simply run without crashing
    run_tonesig_demo()
    captured = capfd.readouterr()
    # Header printed
    assert "Multi-Turn PUTMAN ToneSig™ Demo" in captured.out
    # Exactly 5 turns printed
    assert captured.out.count("=== Turn ") == 5
