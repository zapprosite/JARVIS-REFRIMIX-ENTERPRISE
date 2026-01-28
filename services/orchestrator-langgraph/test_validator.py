from src.validators import validate_rag_response

def test_validator_success():
    inp = {"answer": "Found it.", "citations": [{"source": "manual.pdf"}]}
    assert validate_rag_response(inp) == inp

def test_validator_flags_missing_citations():
    inp = {"answer": "The error code means fan lock.", "citations": []}
    out = validate_rag_response(inp)
    assert "warning" in out
    assert "Low Confidence" in out["warning"]

def test_validator_allows_negative_answer():
    inp = {"answer": "I could not find any information about that code.", "citations": []}
    out = validate_rag_response(inp)
    assert "warning" not in out

def test_validator_sanitizes_bad_citations():
    inp = {
        "answer": "Found.", 
        "citations": [{"source": "ok.pdf"}, "bad_string", {}]
    }
    out = validate_rag_response(inp)
    assert len(out["citations"]) == 1
    assert out["citations"][0]["source"] == "ok.pdf"

if __name__ == "__main__":
    import traceback
    tests = [
        test_validator_success,
        test_validator_flags_missing_citations,
        test_validator_allows_negative_answer,
        test_validator_sanitizes_bad_citations
    ]
    for t in tests:
        try:
            print(f"Running {t.__name__}...", end=" ")
            t()
            print("OK")
        except Exception:
            print("FAIL")
            traceback.print_exc()
            exit(1)
    print("✅ All Validator tests passed!")
