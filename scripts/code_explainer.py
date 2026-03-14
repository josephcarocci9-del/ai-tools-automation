from openai import OpenAI

client = OpenAI()

def explain_code(code):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Explain this code clearly:\n\n{code}"
    )
    return response.output_text

if __name__ == "__main__":
    code = input("Paste code to explain:\n")
    explanation = explain_code(code)
    print("\nExplanation:\n")
    print(explanation)
