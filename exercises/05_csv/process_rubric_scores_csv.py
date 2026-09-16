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

with open("data/rubric_scores.csv", "r", encoding="utf-8", newline="") as scores_file:
    reader = csv.DictReader(scores_file)

    for row in reader:
        scores = {}

        for field in score_fields:
            scores[field] = int(row[field])

        total_score = calculate_total_score(scores)
        percentage = calculate_percentage(total_score, maximum_score)
        decision = "PASS" if passes_threshold(percentage) else "FAIL"

        print(
            f"{row['test_case']} | {total_score}/{maximum_score} "
            f"| {percentage:.1f}% | {decision}"
        )
