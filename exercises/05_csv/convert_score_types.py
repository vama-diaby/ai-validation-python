import csv


with open("data/scores.csv", "r", encoding="utf-8", newline="") as scores_file:
    reader = csv.DictReader(scores_file)

    for row in reader:
        score = row["score"]

        print("Test case:", row["test_case"])
        print("Type before conversion:", type(score))

        score = int(score)

        print("Type after conversion:", type(score))
