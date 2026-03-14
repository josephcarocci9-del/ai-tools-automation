import random

tasks = [
    "Write documentation",
    "Fix a bug",
    "Improve code performance",
    "Refactor a module",
    "Add new automation feature"
]

def generate_task():
    task = random.choice(tasks)
    print("Suggested task:", task)

if __name__ == "__main__":
    generate_task()
