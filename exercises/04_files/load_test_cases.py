def load_test_cases(file_path="data/test_cases.txt"):
    test_cases = []

    with open(file_path, "r", encoding="utf-8") as test_cases_file:
        for line in test_cases_file:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            test_case_id, prompt = cleaned_line.split("|", maxsplit=1)
            test_cases.append(
                {
                    "id": test_case_id,
                    "prompt": prompt,
                }
            )

    return test_cases
