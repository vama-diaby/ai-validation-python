from pathlib import Path


evaluation_results = [
    ("T01", "PASS"),
    ("T02", "FAIL"),
    ("T03", "PASS"),
]

output_path = Path("results/simple_results.txt")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8") as results_file:
    for test_case, decision in evaluation_results:
        results_file.write(f"{test_case} | {decision}\n")

print("Results written to", output_path)
