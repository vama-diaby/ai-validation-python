with open("data/models.txt", "r", encoding="utf-8") as models_file:
    print(type(models_file))

    for line in models_file:
        print(line.strip())
