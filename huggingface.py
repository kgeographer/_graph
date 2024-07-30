from transformers import pipeline

# Load the model
model_name = "gpt-2"
model = pipeline('text-generation', model=model_name)

# Check the model card on Hugging Face
print(model.model_card)