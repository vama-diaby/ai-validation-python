evaluation_record = {
    "experiment_id": "EXP-002",
    "test_case": "instruction_following",
    "model": "model-a",
    "score": 22,
    "maximum_score": 25,
    "passed": True
}

print("Model:", evaluation_record["model"])
print("Score:", evaluation_record["score"])
print("Passed:", evaluation_record["passed"])
