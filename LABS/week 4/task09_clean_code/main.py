from preprocessing import filter_by_confidence, split_complete_records, normalize_labels
from analysis import count_by_label, get_unique_labels, find_unexpected_labels, average_confidence, top_predictions

initial_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58}
]

MIN_CONFIDENCE = 0.80

high_conf = filter_by_confidence(initial_predictions, MIN_CONFIDENCE)
print("Selected IDs:", [p["id"] for p in high_conf])
print("Label counts:", count_by_label(initial_predictions))
print("Unique labels:", get_unique_labels(initial_predictions))

new_batch = [
    {"id": 8, "label": "Spam", "confidence": 0.91},
    {"id": 9, "label": "ham"},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": " HAM ", "confidence": 0.66}
]

ALLOWED_LABELS = {"spam", "ham", "promotion"}
REQUIRED_FIELDS = ("id", "label", "confidence")
TOP_COUNT = 3

combined_data = initial_predictions + new_batch
complete_recs, skipped_ids = split_complete_records(combined_data, REQUIRED_FIELDS)
normalized_recs = normalize_labels(complete_recs)

summary = {
    "total_records": len(combined_data),
    "valid_records": len(normalized_recs),
    "skipped_ids": skipped_ids,
    "labels": get_unique_labels(normalized_recs),
    "label_counts": count_by_label(normalized_recs),
    "high_confidence_count": len(filter_by_confidence(normalized_recs, MIN_CONFIDENCE)),
    "unexpected_labels": find_unexpected_labels(normalized_recs, ALLOWED_LABELS),
    "average_confidence": round(average_confidence(normalized_recs), 3),
    "top_ids": top_predictions(normalized_recs, TOP_COUNT)
}

print("\n=== Prediction Report ===")
print("Total records:", summary["total_records"])
print("Valid records:", summary["valid_records"])
print("Skipped (missing data):", summary["skipped_ids"])
print("Labels:", summary["labels"])
print("Label counts:", summary["label_counts"])
print("High confidence (>= 0.8):", summary["high_confidence_count"])
print("Unexpected labels:", summary["unexpected_labels"])
print("Average confidence:", summary["average_confidence"])
print("Top 3 by confidence:", summary["top_ids"])
print("Raw record 8 label check:", new_batch[0]["label"])