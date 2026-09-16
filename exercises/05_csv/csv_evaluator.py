import csv
from pathlib import Path


SCORE_FIELDS = [
    "instruction_following",
    "relevance",
    "completeness",
    "clarity",
    "format_compliance",
]
RESULT_FIELDS = [
    "experiment_id",
    "test_case",
    "condition",
    "prompt_version",
    "total_score",
    "maximum_score",
    "percentage",
    "status",
]


def load_evaluations(input_file="data/evaluation_scores.csv"):
    evaluations = []

    with open(input_file, "r", encoding="utf-8", newline="") as scores_file:
        reader = csv.DictReader(scores_file)

        for row in reader:
            scores = {}

            for field in SCORE_FIELDS:
                scores[field] = int(row[field])

            evaluations.append(
                {
                    "experiment_id": row["experiment_id"],
                    "test_case": row["test_case"],
                    "condition": row["condition"],
                    "prompt_version": row["prompt_version"],
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
        "experiment_id": evaluation["experiment_id"],
        "test_case": evaluation["test_case"],
        "condition": evaluation["condition"],
        "prompt_version": evaluation["prompt_version"],
        "total_score": total_score,
        "maximum_score": maximum_score,
        "percentage": f"{percentage:.1f}",
        "status": "PASS" if passed else "FAIL",
    }


def calculate_summary(result_records):
    total_evaluations = len(result_records)
    pass_count = 0
    total_percentage = 0

    for result in result_records:
        total_percentage += float(result["percentage"])

        if result["status"] == "PASS":
            pass_count += 1

    failure_count = total_evaluations - pass_count
    pass_rate = calculate_percentage(pass_count, total_evaluations)
    average_percentage = total_percentage / total_evaluations

    return {
        "total_evaluations": total_evaluations,
        "passed": pass_count,
        "failed": failure_count,
        "pass_rate": pass_rate,
        "average_percentage": average_percentage,
    }


def save_results(result_records, output_file="results/evaluation_results.csv"):
    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    with output_path.open("w", encoding="utf-8", newline="") as results_file:
        writer = csv.DictWriter(results_file, fieldnames=RESULT_FIELDS)
        writer.writeheader()
        writer.writerows(result_records)


def save_summary(summary, output_file="results/evaluation_summary.csv"):
    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    summary_rows = [
        {"metric": "total_evaluations", "value": summary["total_evaluations"]},
        {"metric": "passed", "value": summary["passed"]},
        {"metric": "failed", "value": summary["failed"]},
        {"metric": "pass_rate", "value": f"{summary['pass_rate']:.1f}"},
        {
            "metric": "average_percentage",
            "value": f"{summary['average_percentage']:.1f}",
        },
    ]

    with output_path.open("w", encoding="utf-8", newline="") as summary_file:
        writer = csv.DictWriter(summary_file, fieldnames=["metric", "value"])
        writer.writeheader()
        writer.writerows(summary_rows)


def save_failed_results(result_records, output_file="results/failed_cases.csv"):
    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    with output_path.open("w", encoding="utf-8", newline="") as failed_cases_file:
        writer = csv.DictWriter(failed_cases_file, fieldnames=RESULT_FIELDS)
        writer.writeheader()

        for result in result_records:
            if result["status"] == "FAIL":
                writer.writerow(result)


def process_evaluations(
    input_file="data/evaluation_scores.csv",
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
    save_results(result_records)
    save_summary(summary)
    save_failed_results(result_records)

    return result_records, summary


if __name__ == "__main__":
    process_evaluations()
