import csv
from importlib import import_module
from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

evaluation_functions = import_module("exercises.02_functions.evaluation_functions")
calculate_percentage = evaluation_functions.calculate_percentage
passes_threshold = evaluation_functions.passes_threshold

maximum_score = 25
output_path = Path("results/scores_processed.csv")
output_path.parent.mkdir(exist_ok=True)

with open("data/scores.csv", "r", encoding="utf-8", newline="") as scores_file:
    reader = csv.DictReader(scores_file)

    with output_path.open("w", encoding="utf-8", newline="") as results_file:
        fieldnames = [
            "test_case",
            "score",
            "maximum_score",
            "percentage",
            "status",
        ]
        writer = csv.DictWriter(results_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            score = int(row["score"])
            percentage = calculate_percentage(score, maximum_score)
            status = "PASS" if passes_threshold(percentage) else "FAIL"

            writer.writerow(
                {
                    "test_case": row["test_case"],
                    "score": score,
                    "maximum_score": maximum_score,
                    "percentage": f"{percentage:.1f}",
                    "status": status,
                }
            )
