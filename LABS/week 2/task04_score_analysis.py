scores = [0.72, 0.81, 0.88, 0.91, 0.67, 0.86, 0.79]
threshold = 0.85

above = 0
below = 0
total_score = 0

for s in scores:
    if s >= threshold:
        above += 1
    else:
        below += 1
    total_score += s

avg = total_score / len(scores)
percentage = (above / len(scores)) * 100

print("Meeting target:", above)
print("Below target:", below)
print(f"Average score: {avg:.2f}")
print(f"Percentage meeting target: {percentage:.2f}%")