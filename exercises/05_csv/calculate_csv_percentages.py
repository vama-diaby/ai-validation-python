import csv
from importlib import import_module
from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

calculate_percentage = import_module(
    "exercises.02_functions.evaluation_functions"
).calculate_percentage

maximum_score = 25

with open("data/scores.csv", "r", encoding="utf-8", newline="") as scores_file:
    reader = csv.DictReader(scores_file)

    for row in reader:
        score = int(row["score"])
        percentage = calculate_percentage(score, maximum_score)
        print(f"{row['test_case']} → {percentage:.1f}%")
