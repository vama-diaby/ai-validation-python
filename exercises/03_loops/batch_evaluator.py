def calculate_total_score(scores):
    return sum(scores.values())


def calculate_percentage(score, maximum):
    return score / maximum * 100


def passes_threshold(percentage, threshold=80):
    return percentage >= threshold


def create_result_record(evaluation, total_score, maximum_score, percentage, passed):
    return {
        "test_case": evaluation["test_case"],
        "condition": evaluation["condition"],
        "scores": evaluation["scores"],
        "total_score": total_score,
        "maximum_score": maximum_score,
        "percentage": percentage,
        "passed": passed,
        "decision": "PASS" if passed else "FAIL",
    }


evaluations = [
    {
        "test_case": "T01",
        "condition": "structured",
        "scores": {
            "instruction_following": 5,
            "relevance": 5,
            "completeness": 4,
            "clarity": 5,
            "format_compliance": 5,
        },
    },
    {
        "test_case": "T02",
        "condition": "structured",
        "scores": {
            "instruction_following": 4,
            "relevance": 4,
            "completeness": 4,
            "clarity": 4,
            "format_compliance": 4,
        },
    },
    {
        "test_case": "T03",
        "condition": "unstructured",
        "scores": {
            "instruction_following": 3,
            "relevance": 4,
            "completeness": 3,
            "clarity": 4,
            "format_compliance": 4,
        },
    },
    {
        "test_case": "T04",
        "condition": "structured",
        "scores": {
            "instruction_following": 5,
            "relevance": 4,
            "completeness": 5,
            "clarity": 4,
            "format_compliance": 5,
        },
    },
    {
        "test_case": "T05",
        "condition": "unstructured",
        "scores": {
            "instruction_following": 4,
            "relevance": 4,
            "completeness": 3,
            "clarity": 4,
            "format_compliance": 4,
        },
    },
]

pass_threshold = 80
maximum_score = 25
result_records = []

for evaluation in evaluations:
    total_score = calculate_total_score(evaluation["scores"])
    percentage = calculate_percentage(total_score, maximum_score)
    passed = passes_threshold(percentage, pass_threshold)
    result_record = create_result_record(
        evaluation,
        total_score,
        maximum_score,
        percentage,
        passed,
    )
    result_records.append(result_record)

total_evaluations = len(result_records)
pass_count = sum(result["passed"] for result in result_records)
failure_count = total_evaluations - pass_count
pass_rate = calculate_percentage(pass_count, total_evaluations)
average_percentage = sum(result["percentage"] for result in result_records) / total_evaluations
failed_cases = [
    result["test_case"] for result in result_records if not result["passed"]
]

print("AI Validation Batch Summary")
print("---------------------------")
print()

for result in result_records:
    print(
        f"{result['test_case']} | {result['total_score']}/{result['maximum_score']} "
        f"| {result['percentage']:.1f}% | {result['decision']}"
    )

print()
print("Summary")
print("-------")
print("Total Evaluations:", total_evaluations)
print("Passed:", pass_count)
print("Failed:", failure_count)
print(f"Pass Rate: {pass_rate:.1f}%")
print(f"Average Score: {average_percentage:.1f}%")
print()
print("Failed Cases")
print("------------")

for test_case in failed_cases:
    print(test_case)
