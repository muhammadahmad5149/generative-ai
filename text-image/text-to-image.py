from diffusers import StableDiffusionPipeline
import torch

# Load the pre-trained model from Hugging Face
model_name = "runwayml/stable-diffusion-v1-5"  # Replace with the desired model
pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float32)
pipe = pipe.to("cpu")  # Move the pipeline to GPU for faster generation

# Prompt for image generation
prompt = "A dense forest at sunrise, ultra-realistic, high detail"

# Generate the image
image = pipe(prompt).images[0]

# Save the generated image
output_path = "generated_image.png"
image.save(output_path)

print(f"Image saved at {output_path}")
