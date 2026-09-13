instruction_following = 4
relevance = 5
completeness = 4
clarity = 4
format_compliance = 5

total_score = instruction_following + relevance + completeness + clarity + format_compliance
maximum_score = 5 * 5
percentage = total_score / maximum_score * 100
pass_threshold = 80
passed = percentage >= pass_threshold

print("Total score:", total_score)
print("Maximum score:", maximum_score)
print("Percentage:", percentage)
print("Passed:", passed)
