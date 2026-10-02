from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

print("Loading image captioning model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

image_path = input("Enter image path: ")

image = Image.open(image_path).convert("RGB")

inputs = processor(
    images=image,
    return_tensors="pt"
)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=50
    )

caption = processor.decode(
    output[0],
    skip_special_tokens=True
)

print("\nGenerated Caption:")
print(caption)