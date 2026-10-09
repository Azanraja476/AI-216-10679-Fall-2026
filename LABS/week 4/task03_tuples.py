import copy

image_size = (224, 224)
model_result = ("baseline_cnn", 0.91)

width, height = image_size
model_name, accuracy = model_result

print(f"Image size: {width} x {height}")
print(f"Model: {model_name} | Accuracy: {accuracy}")

def summarize_scores(scores):
    if not scores:
        return None
    return min(scores), max(scores), sum(scores) / len(scores)

print("Minimum:", summarize_scores([72, 88, 91, 67])[0], "| Maximum:", summarize_scores([72, 88, 91, 67])[1], "| Average:", summarize_scores([72, 88, 91, 67])[2])
print("Empty:", summarize_scores([]))

input_models = {
    (224, 224): "resnet50",
    (299, 299): "inception_v3",
    (384, 384): "vit_base"
}

print("Model for 299x299:", input_models.get((299, 299)))

try:
    invalid_dict = {[224, 224]: "resnet50"}
except TypeError as e:
    print("TypeError:", e)