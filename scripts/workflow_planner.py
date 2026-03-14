import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_workflow(goal):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
You are an expert productivity assistant.

Create a clear step-by-step workflow to achieve the following goal:

{goal}

Structure the response like this:

1. Goal overview
2. Step-by-step plan
3. Recommended tools
4. Tips for efficiency
"""
    )

    return response.output_text


def save_plan(goal, plan):
    filename = "workflow_plan.txt"

    with open(filename, "w") as f:
        f.write(f"Goal: {goal}\n\n")
        f.write(plan)

    print(f"\nWorkflow saved to {filename}")


def main():
    print("\nAI Workflow Planner")
    print("-------------------")

    goal = input("What goal do you want to plan?\n> ")

    print("\nGenerating workflow...\n")

    plan = generate_workflow(goal)

    print(plan)

    save_plan(goal, plan)


if __name__ == "__main__":
    main()
