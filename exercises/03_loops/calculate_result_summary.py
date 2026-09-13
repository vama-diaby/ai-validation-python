results = [
    True,
    False,
    True,
    True,
    False,
    True,
]

total = len(results)
passes = 0

for result in results:
    if result:
        passes += 1

failures = total - passes
pass_rate = passes / total * 100

print("Total:", total)
print("Passes:", passes)
print("Failures:", failures)
print("Pass Rate:", f"{pass_rate:.1f}%")
