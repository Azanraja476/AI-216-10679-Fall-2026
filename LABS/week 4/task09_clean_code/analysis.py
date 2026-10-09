def count_by_label(predictions):
    counts = {}
    for p in predictions:
        lbl = p["label"]
        counts[lbl] = counts.get(lbl, 0) + 1
    return counts

def get_unique_labels(predictions):
    return sorted(list({p["label"] for p in predictions}))

def find_unexpected_labels(predictions, allowed_labels):
    current_labels = {p["label"] for p in predictions}
    return sorted(list(current_labels - allowed_labels))

def average_confidence(predictions):
    if not predictions:
        return None
    total = sum(p["confidence"] for p in predictions)
    return total / len(predictions)

def top_predictions(predictions, count):
    sorted_preds = sorted(predictions, key=lambda x: x["confidence"], reverse=True)
    return [p["id"] for p in sorted_preds[:count]]