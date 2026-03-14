import os
import sys
import logging
from openai import OpenAI

# -------------------------------------------------
# Configuration
# -------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    print("ERROR: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

client = OpenAI(api_key=API_KEY)

MODEL = "gpt-4.1-mini"


# -------------------------------------------------
# Core AI interaction
# -------------------------------------------------

def ask_ai(prompt):
    """
    Sends a prompt to the OpenAI API and returns the response text.
    """

    try:
        response = client.responses.create(
            model=MODEL,
            input=prompt
        )

        return response.output_text

    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return "Error communicating with the AI service."


# -------------------------------------------------
# AI Tools
# -------------------------------------------------

def explain_code():
    print("\nPaste the code you want explained.")
    print("Finish with an empty line.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    code = "\n".join(lines)

    prompt = f"""
Explain the following code clearly for a developer.

Code:
{code}
"""

    print("\nAI Explanation:\n")
    print(ask_ai(prompt))


def summarize_text():
    print("\nPaste the text to summarize.")
    print("Finish with an empty line.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    prompt = f"""
Summarize the following text clearly and concisely:

{text}
"""

    print("\nSummary:\n")
    print(ask_ai(prompt))


def generate_email():
    topic = input("\nEmail topic: ")

    prompt = f"""
Write a professional email about the following topic:

{topic}
"""

    print("\nGenerated Email:\n")
    print(ask_ai(prompt))


def plan_workflow():
    goal = input("\nGoal you want to achieve: ")

    prompt = f"""
Create a step-by-step productivity workflow to achieve this goal:

{goal}

Include tools and efficiency tips.
"""

    print("\nWorkflow Plan:\n")
    print(ask_ai(prompt))


def generate_prompt():
    topic = input("\nTopic for AI prompt: ")

    prompt = f"""
Generate a creative and useful AI prompt about:

{topic}
"""

    print("\nGenerated Prompt:\n")
    print(ask_ai(prompt))


# -------------------------------------------------
# CLI Interface
# -------------------------------------------------

def print_menu():
    print("\nAI Automation Assistant")
    print("-----------------------")
    print("1 - Explain code")
    print("2 - Summarize text")
    print("3 - Generate email")
    print("4 - Plan workflow")
    print("5 - Generate AI prompt")
    print("6 - Exit")


def main():
    logging.info("Starting AI Automation Assistant")

    while True:

        print_menu()

        choice = input("\nSelect option: ").strip()

        if choice == "1":
            explain_code()

        elif choice == "2":
            summarize_text()

        elif choice == "3":
            generate_email()

        elif choice == "4":
            plan_workflow()

        elif choice == "5":
            generate_prompt()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


# -------------------------------------------------

if __name__ == "__main__":
    main()
