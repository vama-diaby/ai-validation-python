def create_evaluation_result(
    experiment_id,
    test_case,
    model,
    percentage,
    passed,
):
    return {
        "experiment_id": experiment_id,
        "test_case": test_case,
        "model": model,
        "percentage": percentage,
        "passed": passed,
    }

