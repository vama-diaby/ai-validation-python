from pathlib import Path


def save_results(results, output_file="results/processed_results.txt"):
    output_path = Path(output_file)
    output_path.parent.mkdir(exist_ok=True)

    with output_path.open("w", encoding="utf-8") as results_file:
        for result in results:
            decision = "PASS" if result["passed"] else "FAIL"
            results_file.write(
                f"{result['test_case']} | {result['percentage']}% | {decision}\n"
            )


results = [
    {
        "test_case": "T01",
        "percentage": 96,
        "passed": True,
    },
    {
        "test_case": "T02",
        "percentage": 76,
        "passed": False,
    },
]

save_results(results)
