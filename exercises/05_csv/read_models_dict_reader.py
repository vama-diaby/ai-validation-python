import csv


with open("data/models.csv", "r", encoding="utf-8", newline="") as models_file:
    reader = csv.DictReader(models_file)

    for row in reader:
        print(f"{row['model_id']} → {row['model_name']}")
