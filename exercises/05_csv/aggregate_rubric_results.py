import csv
from importlib import import_module
from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

evaluation_functions = import_module("exercises.02_functions.evaluation_functions")
calculate_total_score = evaluation_functions.calculate_total_score
calculate_percentage = evaluation_functions.calculate_percentage
passes_threshold = evaluation_functions.passes_threshold

score_fields = [
    "instruction_following",
    "relevance",
    "completeness",
    "clarity",
    "format_compliance",
]
maximum_score = 25
processed_records = []

with open("data/rubric_scores.csv", "r", encoding="utf-8", newline="") as scores_file:
    reader = csv.DictReader(scores_file)

    for row in reader:
        scores = {}

        for field in score_fields:
            scores[field] = int(row[field])

        total_score = calculate_total_score(scores)
        percentage = calculate_percentage(total_score, maximum_score)
        passed = passes_threshold(percentage)

        processed_records.append(
            {
                "test_case": row["test_case"],
                "total_score": total_score,
                "percentage": percentage,
                "passed": passed,
            }
        )

total_evaluations = len(processed_records)
pass_count = 0
total_percentage = 0

for record in processed_records:
    total_percentage += record["percentage"]

    if record["passed"]:
        pass_count += 1

failure_count = total_evaluations - pass_count
pass_rate = calculate_percentage(pass_count, total_evaluations)
average_percentage = total_percentage / total_evaluations

output_path = Path("results/failed_cases.csv")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8", newline="") as failed_cases_file:
    fieldnames = ["test_case", "total_score", "percentage", "status"]
    writer = csv.DictWriter(failed_cases_file, fieldnames=fieldnames)
    writer.writeheader()

    for record in processed_records:
        if not record["passed"]:
            writer.writerow(
                {
                    "test_case": record["test_case"],
                    "total_score": record["total_score"],
                    "percentage": f"{record['percentage']:.1f}",
                    "status": "FAIL",
                }
            )

print("Total Evaluations:", total_evaluations)
print("Pass Count:", pass_count)
print("Failure Count:", failure_count)
print(f"Pass Rate: {pass_rate:.1f}%")
print(f"Average Percentage: {average_percentage:.1f}%")
