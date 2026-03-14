import random

prompts = [
    "Write a story about a futuristic city.",
    "Explain a complex concept in simple terms.",
    "Generate startup ideas using AI.",
    "Create a productivity workflow using automation."
]

def generate_prompt():
    prompt = random.choice(prompts)
    print("Generated Prompt:")
    print(prompt)

if __name__ == "__main__":
    generate_prompt()
