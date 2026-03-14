from openai import OpenAI

client = OpenAI()

def plan_tasks(goal):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Create a step-by-step plan to achieve this goal: {goal}"
    )
    return response.output_text

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    plan = plan_tasks(goal)

    print("\nPlan:\n")
    print(plan)
