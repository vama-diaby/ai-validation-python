def calculate_total(scores):
    return sum(scores)


def calculate_percentage(total_score, maximum_score):
    return total_score / maximum_score * 100


def is_passing(percentage, threshold):
    return percentage >= threshold


scores = [4, 5, 4, 5, 4]
maximum_score = 25
threshold = 80

total_score = calculate_total(scores)
percentage = calculate_percentage(total_score, maximum_score)
passed = is_passing(percentage, threshold)

print("Total score:", total_score)
print("Percentage:", str(percentage) + "%")
print("Passed:", passed)
