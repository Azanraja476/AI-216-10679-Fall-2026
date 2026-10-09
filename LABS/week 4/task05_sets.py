training_labels = ["spam", "ham", "spam", "promotion", "ham"]
test_labels = ["spam", "ham", "unknown", "promotion"]

train_set = set(training_labels)
test_set = set(test_labels)

print("Unique training labels:", sorted(list(train_set)))
print("In both:", sorted(list(train_set & test_set)))
print("Only in test:", sorted(list(test_set - train_set)))
print("In either:", sorted(list(train_set | test_set)))