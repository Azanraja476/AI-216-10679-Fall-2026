accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]
THRESHOLD = 0.85

print("First:", accuracies[0])
print("Last:", accuracies[-1])
print("Middle four:", accuracies[1:5])

accuracies.append(0.89)
accuracies.extend([0.84, 0.90])

target_index = accuracies.index(0.78)
accuracies[target_index] = 0.80

print("Updated:", accuracies)

count_above = sum(1 for a in accuracies if a >= THRESHOLD)
print(f"Scores >= {THRESHOLD}:", count_above)

print("Highest:", max(accuracies))
print("Lowest:", min(accuracies))

sorted_desc = sorted(accuracies, reverse=True)
print("Sorted (high to low):", sorted_desc)
print("Original order kept:", accuracies)