rubric_scores = {
    "instruction_following": 5,
    "relevance": 4,
    "completeness": 5,
    "clarity": 4,
    "format_compliance": 5,
}

for criterion, score in rubric_scores.items():
    print(f"{criterion}: {score}/5")
