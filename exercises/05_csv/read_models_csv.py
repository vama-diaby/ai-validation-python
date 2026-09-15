import csv


with open("data/models.csv", "r", encoding="utf-8", newline="") as models_file:
    reader = csv.reader(models_file)

    for row in reader:
        print(row)
