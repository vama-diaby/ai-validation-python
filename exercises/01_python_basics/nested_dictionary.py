evaluation_record = {
    "test_case": "T01",
    "condition": "Structured",
    "scores": {
        "instruction_following": 5,
        "relevance": 4,
        "completeness": 5,
        "clarity": 5,
        "format_compliance": 4
    }
}

print("Test Case:", evaluation_record["test_case"])
print("Condition:", evaluation_record["condition"])
print("Instruction Following:", evaluation_record["scores"]["instruction_following"])
print("Relevance:", evaluation_record["scores"]["relevance"])
print("Completeness:", evaluation_record["scores"]["completeness"])
print("Clarity:", evaluation_record["scores"]["clarity"])
print("Format Compliance:", evaluation_record["scores"]["format_compliance"])
