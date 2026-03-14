import os
from openai import OpenAI

client = OpenAI()

def ask_ai(prompt):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"Error: {e}"

def main():
    print("AI Assistant Tool")
    print("Type your question (or 'exit' to quit):")

    while True:
        user_input = input("\n> ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        answer = ask_ai(user_input)
        print("\nAI:", answer)

if __name__ == "__main__":
    main()
