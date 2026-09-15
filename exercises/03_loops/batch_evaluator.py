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


def process_evaluations(evaluations, maximum_score=25, pass_threshold=80):
    """Process supplied records without defining evaluation data in this module."""
    result_records = []

    for evaluation in evaluations:
        total_score = calculate_total_score(evaluation["scores"])
        percentage = calculate_percentage(total_score, maximum_score)
        passed = passes_threshold(percentage, pass_threshold)
        result_records.append(
            create_result_record(
                evaluation,
                total_score,
                maximum_score,
                percentage,
                passed,
            )
        )

    return result_records
