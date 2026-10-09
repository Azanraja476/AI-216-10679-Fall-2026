def calculate_percentage(obtained, total):
    if total == 0:
        return 0.0
    return (obtained / total) * 100

def is_passing(score, passing_score):
    return score >= passing_score

choice = ""
while choice != "3":
    print("1. Check pass/fail")
    print("2. Calculate percentage")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        s = float(input("Score: "))
        p = float(input("Passing score: "))
        print("Result:", is_passing(s, p))
    elif choice == "2":
        obt = float(input("Obtained: "))
        tot = float(input("Total: "))
        print("Percentage:", f"{calculate_percentage(obt, tot):.2f}%")
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice, try again.")