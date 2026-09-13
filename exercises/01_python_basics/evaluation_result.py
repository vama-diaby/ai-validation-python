experiment_id = "EXP-001"
test_case = "T01"
condition = "Structured"
model = "model-a"

instruction_following = 5
relevance = 5
completeness = 4
clarity = 5
format_compliance = 5

total_score = instruction_following + relevance + completeness + clarity + format_compliance
maximum_score = 25
percentage = total_score / maximum_score * 100
pass_threshold = 80
passed = percentage >= pass_threshold

if passed:
    decision = "PASS"
else:
    decision = "FAIL"

print("AI Evaluation Result")
print("--------------------")
print("Experiment:", experiment_id)
print("Test Case:", test_case)
print("Condition:", condition)
print("Model:", model)
print()
print("Instruction Following:", str(instruction_following) + "/5")
print("Relevance:", str(relevance) + "/5")
print("Completeness:", str(completeness) + "/5")
print("Clarity:", str(clarity) + "/5")
print("Format Compliance:", str(format_compliance) + "/5")
print()
print("Total:", str(total_score) + "/" + str(maximum_score))
print("Percentage:", str(percentage) + "%")
print("Decision:", decision)
