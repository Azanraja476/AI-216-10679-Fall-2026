evaluation_order = ["model_a", "model_b", "model_c"]
fixed_resolution = (224, 224)
model_metadata = {"name": "resnet", "threshold": 0.5, "version": 1}
unique_classes = {"spam", "ham", "promotion"}

print("Evaluation Order:", evaluation_order)
print("Resolution:", fixed_resolution)
print("Metadata:", model_metadata)
print("Classes:", unique_classes)