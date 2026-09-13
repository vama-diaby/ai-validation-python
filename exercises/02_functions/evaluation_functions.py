def calculate_total_score(scores):
    """Calculate the total rubric score."""
    return sum(scores.values())


def calculate_percentage(total_score, maximum_score):
    """Convert a total score into a percentage."""
    return total_score / maximum_score * 100


def passes_threshold(percentage, threshold=80):
    """Return whether a percentage meets the acceptance threshold."""
    return percentage >= threshold


def create_evaluation_result(
    experiment_id,
    test_case,
    model,
    scores,
    maximum_score,
    threshold=80,
):
    """Return the calculated evaluation results in structured form."""
    total_score = calculate_total_score(scores)
    percentage = calculate_percentage(total_score, maximum_score)
    passed = passes_threshold(percentage, threshold)

    return {
        "experiment_id": experiment_id,
        "test_case": test_case,
        "model": model,
        "scores": scores,
        "total_score": total_score,
        "maximum_score": maximum_score,
        "percentage": percentage,
        "threshold": threshold,
        "passed": passed,
    }
