raw_scores = [78, -5, 92, 110, 67, 85]

valid = [s for s in raw_scores if 0 <= s <= 100]
normalized = [s / 100 for s in valid]

print("Valid:", valid)
print("Normalized:", normalized)

student_scores = {"Ali": 72, "Sara": 91, "Ahmed": 45, "Fatima": 88}
pass_status = {name: score >= 50 for name, score in student_scores.items()}
print("Pass status:", pass_status)

labels = ["Spam", "HAM", "spam", "Ham", "UNKNOWN"]
unique_lower = {l.lower() for l in labels}
print("Labels:", sorted(list(unique_lower)))