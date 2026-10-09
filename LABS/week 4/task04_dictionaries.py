model_info = {
    "name": "spam_classifier",
    "version": 2,
    "accuracy": 0.92,
    "threshold": 0.80,
    "status": "evaluated"
}

print("Name:", model_info["name"])

model_info["accuracy"] = 0.94
model_info["owner"] = "AI-216 Team"

print("Owner (using get):", model_info.get("owner", "Unknown"))

model_info["metrics"] = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89
}

print("Precision:", model_info["metrics"]["precision"])
print("Recall:", model_info["metrics"]["recall"])