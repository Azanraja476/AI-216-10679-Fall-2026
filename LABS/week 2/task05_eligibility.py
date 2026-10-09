age = 19
score = 72
prerequisite = True

if age >= 18 and score >= 60 and prerequisite:
    print("Result: Eligible")
else:
    print("Result: Not eligible")
    if age < 18:
        print("- Age requirement not met")
    if score < 60:
        print("- Programming score requirement not met")
    if not prerequisite:
        print("- Prerequisite course not completed")