experiments = [0.81, 0.86, 0.79, 0.91]

for idx, exp in enumerate(experiments, start=1):
    print(f"Experiment {idx}: {exp}")

predictions = [True, False, True, True]
actual = [True, False, False, True]

correct_count = 0
for pred, act in zip(predictions, actual):
    is_correct = pred == act
    if is_correct:
        correct_count += 1
    print(f"Predicted: {pred} | Actual: {act} | Correct: {is_correct}")

accuracy = (correct_count / len(predictions)) * 100
print(f"Accuracy: {accuracy:.2f}%")