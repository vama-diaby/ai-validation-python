def calculate_percentage(score, maximum):
    return score / maximum * 100


def passes_threshold(percentage, threshold=80):
    return percentage >= threshold


scores = [
    24,
    20,
    18,
    25,
    21,
]
maximum_score = 25

for score in scores:
    percentage = calculate_percentage(score, maximum_score)
    decision = "PASS" if passes_threshold(percentage) else "FAIL"
    print(f"{score}/{maximum_score} → {percentage:.1f}% → {decision}")
