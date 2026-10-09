def calculate_average(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

def find_highest(scores):
    if len(scores) == 0:
        return None
    return max(scores)

def count_above_threshold(scores, threshold):
    return sum(1 for s in scores if s >= threshold)

def classify_average(average):
    if average is None:
        return "No valid data"
    elif average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Satisfactory"
    else:
        return "Needs Improvement"

scores = [78, 85, 92, 67, 88]
avg = calculate_average(scores)
print("Average:", avg)
print("Highest:", find_highest(scores))
print("Above 80:", count_above_threshold(scores, 80))
print("Classification:", classify_average(avg))