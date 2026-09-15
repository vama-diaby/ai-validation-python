from pathlib import Path


def load_evaluations(file_path="data/evaluation_scores.txt"):
    evaluations = []

    with open(file_path, "r", encoding="utf-8") as scores_file:
        headers = scores_file.readline().strip().split("|")
        score_fields = headers[1:]

        for line in scores_file:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            values = cleaned_line.split("|")
            scores = {
                field: int(value)
                for field, value in zip(score_fields, values[1:])
            }
            evaluations.append(
                {
                    "test_case": values[0],
                    "scores": scores,
                }
            )

    return evaluations


def calculate_total_score(scores):
    return sum(scores.values())


def calculate_percentage(score, maximum_score):
    return score / maximum_score * 100


def passes_threshold(percentage, threshold=80):
    return percentage >= threshold


def create_result_record(evaluation, total_score, maximum_score, percentage, passed):
    return {
        "test_case": evaluation["test_case"],
        "scores": evaluation["scores"],
        "total_score": total_score,
        "maximum_score": maximum_score,
        "percentage": percentage,
        "passed": passed,
        "decision": "PASS" if passed else "FAIL",
    }


def calculate_summary(result_records):
    total_evaluations = len(result_records)
    pass_count = sum(result["passed"] for result in result_records)
    failure_count = total_evaluations - pass_count
    pass_rate = calculate_percentage(pass_count, total_evaluations)
    average_percentage = (
        sum(result["percentage"] for result in result_records) / total_evaluations
    )
    failed_cases = [
        result["test_case"] for result in result_records if not result["passed"]
    ]

    return {
        "total_evaluations": total_evaluations,
        "pass_count": pass_count,
        "failure_count": failure_count,
        "pass_rate": pass_rate,
        "average_percentage": average_percentage,
        "failed_cases": failed_cases,
    }


def save_results(result_records, summary, output_file="results/evaluation_results.txt"):
    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    with output_path.open("w", encoding="utf-8") as results_file:
        results_file.write("AI Validation Batch Results\n")
        results_file.write("===========================\n\n")

        for result in result_records:
            results_file.write(
                f"{result['test_case']} | {result['total_score']}/"
                f"{result['maximum_score']} | {result['percentage']:.1f}% | "
                f"{result['decision']}\n"
            )

        results_file.write("\nSummary\n")
        results_file.write("-------\n")
        results_file.write(f"Total Evaluations: {summary['total_evaluations']}\n")
        results_file.write(f"Passed: {summary['pass_count']}\n")
        results_file.write(f"Failed: {summary['failure_count']}\n")
        results_file.write(f"Pass Rate: {summary['pass_rate']:.1f}%\n")
        results_file.write(
            f"Average Percentage: {summary['average_percentage']:.1f}%\n"
        )
        results_file.write("\nFailed Cases\n")
        results_file.write("------------\n")

        for test_case in summary["failed_cases"]:
            results_file.write(test_case + "\n")


def process_evaluations(
    input_file="data/evaluation_scores.txt",
    output_file="results/evaluation_results.txt",
    maximum_score=25,
    threshold=80,
):
    evaluations = load_evaluations(input_file)
    result_records = []

    for evaluation in evaluations:
        total_score = calculate_total_score(evaluation["scores"])
        percentage = calculate_percentage(total_score, maximum_score)
        passed = passes_threshold(percentage, threshold)
        result_records.append(
            create_result_record(
                evaluation,
                total_score,
                maximum_score,
                percentage,
                passed,
            )
        )

    summary = calculate_summary(result_records)
    save_results(result_records, summary, output_file)

    return result_records, summary
