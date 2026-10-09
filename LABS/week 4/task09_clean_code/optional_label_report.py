records = [
    {"label": "spam", "confidence": 0.94},
    {"label": "ham", "confidence": 0.72},
    {"label": "spam", "confidence": 0.89},
    {"label": "ham", "confidence": 0.97},
    {"label": "unknown", "confidence": 0.86},
    {"label": "ham", "confidence": 0.66}
]

grouped = {}
for r in records:
    l = r["label"]
    if l not in grouped:
        grouped[l] = []
    grouped[l].append(r["confidence"])

print("Label       Count  Avg_Conf  Max_Conf")
for l in sorted(grouped.keys()):
    confs = grouped[l]
    print(f"{l:<11} {len(confs):<6} {sum(confs)/len(confs):<9.3f} {max(confs)}")