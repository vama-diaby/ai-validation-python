evaluations = [
    {"test_case": "T01", "condition": "baseline", "percentage": 80},
    {"test_case": "T01", "condition": "structured", "percentage": 96},
    {"test_case": "T02", "condition": "baseline", "percentage": 72},
    {"test_case": "T02", "condition": "structured", "percentage": 88},
    {"test_case": "T03", "condition": "baseline", "percentage": 76},
    {"test_case": "T03", "condition": "structured", "percentage": 92},
]

results_by_condition = {
    "baseline": 0,
    "structured": 0,
}

for evaluation in evaluations:
    condition = evaluation["condition"]
    results_by_condition[condition] += 1

print("Results by condition")

for condition, count in results_by_condition.items():
    print(f"{condition.title()}: {count}")
