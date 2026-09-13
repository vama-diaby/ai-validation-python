models = [
    "model-a",
    "model-b",
]

test_cases = [
    "T01",
    "T02",
    "T03",
]

total_executions = 0

for model in models:
    for test_case in test_cases:
        for run_number in range(1, 4):
            print(f"{model} | {test_case} | Run {run_number}")
            total_executions += 1

print("Total executions:", total_executions)
