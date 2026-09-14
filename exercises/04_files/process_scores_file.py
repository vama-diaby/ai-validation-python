from pathlib import Path


def calculate_percentage(score, maximum_score=25):
    return score / maximum_score * 100


def passes_threshold(percentage, threshold=80):
    return percentage >= threshold


def process_scores(input_file="data/scores.txt", output_file="results/processed_scores.txt"):
    processed_results = []

    with open(input_file, "r", encoding="utf-8") as scores_file:
        for line in scores_file:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            test_case, score_text = cleaned_line.split("|", maxsplit=1)
            score = int(score_text)
            percentage = calculate_percentage(score)
            passed = passes_threshold(percentage)

            processed_results.append(
                {
                    "test_case": test_case,
                    "score": score,
                    "percentage": percentage,
                    "passed": passed,
                    "decision": "PASS" if passed else "FAIL",
                }
            )

    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    with output_path.open("w", encoding="utf-8") as results_file:
        for result in processed_results:
            results_file.write(
                f"{result['test_case']}|{result['score']}|"
                f"{result['percentage']:.1f}|{result['decision']}\n"
            )

    return processed_results


if __name__ == "__main__":
    process_scores()
