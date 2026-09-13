results = [
    {"test_case": "T01", "percentage": 96},
    {"test_case": "T02", "percentage": 78},
    {"test_case": "T03", "percentage": 80},
    {"test_case": "T04", "percentage": 64},
    {"test_case": "T05", "percentage": 92},
]

pass_threshold = 80
failed_cases = []

for result in results:
    if result["percentage"] < pass_threshold:
        failed_cases.append(result["test_case"])

for failed_test in failed_cases:
    print(failed_test)
