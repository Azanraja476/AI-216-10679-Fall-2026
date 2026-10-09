def filter_by_confidence(predictions, min_confidence):
    return [p for p in predictions if p["confidence"] >= min_confidence]

def split_complete_records(predictions, required_fields):
    complete = []
    skipped_ids = []
    for p in predictions:
        if all(field in p for field in required_fields):
            complete.append(p)
        else:
            skipped_ids.append(p.get("id"))
    return complete, skipped_ids

def normalize_labels(predictions):
    normalized = []
    for p in predictions:
        copy_rec = p.copy()
        copy_rec["label"] = copy_rec["label"].strip().lower()
        normalized.append(copy_rec)
    return normalized