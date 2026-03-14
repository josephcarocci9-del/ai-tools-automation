# AI Automation Tool
# Maintained by Joseph Carocci

import datetime
import os

def show_banner():
    print("===================================")
    print("      AI AUTOMATION TOOL")
    print("===================================")
    print("Author: Joseph Carocci")
    print("Open Source Automation Project")
    print()

def log_task(task_name):
    now = datetime.datetime.now()
    log_line = f"[{now}] Task executed: {task_name}\n"

    with open("automation_log.txt", "a") as log_file:
        log_file.write(log_line)

def automate_task(task_name):
    print(f"Running automation for: {task_name}")
    log_task(task_name)
    print("Task completed and logged.")
    print()

def system_info():
    print("System information:")
    print("Operating System:", os.name)
    print("Current directory:", os.getcwd())
    print()

def menu():
    while True:
        print("Select an option:")
        print("1 - Run automation task")
        print("2 - Show system info")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task name: ")
            automate_task(task)

        elif choice == "2":
            system_info()

        elif choice == "3":
            print("Exiting automation tool.")
            break

        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    show_banner()
    menu()
