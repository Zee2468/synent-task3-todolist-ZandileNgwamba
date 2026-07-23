# Task Manager Functions
# Author: Zandile Ngwamba
# Internship Task 3

import json

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    return tasks


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    """Add a new task."""

    tasks = load_tasks()

    task = input("\nEnter your task: ")

    new_task = {
        "task": task,
        "completed": False
    }

    tasks.append(new_task)

    save_tasks(tasks)

    print("\n✅ Task Added Successfully!")


def complete_task():
    """Mark a task as completed."""

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo tasks to complete.")
        return

    print("\n========== TASKS ==========\n")

    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['task']} {status}")

    try:
        number = int(input("\nEnter task number to complete: "))

        if 1 <= number <= len(tasks):

            tasks[number - 1]["completed"] = True

            save_tasks(tasks)

            print("\n🎉 Task marked as completed!")

        else:
            print("\n❌ Invalid task number.")

    except ValueError:
        print("\n❌ Please enter a valid number.")


def delete_task():
    """Delete a task."""

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    print("\n========== TASKS ==========\n")

    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['task']} {status}")

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):

            deleted = tasks.pop(number - 1)

            save_tasks(tasks)

            print(f"\n🗑️ '{deleted['task']}' deleted successfully!")

        else:
            print("\n❌ Invalid task number.")

    except ValueError:
        print("\n❌ Please enter a valid number.")

def search_task():
    """Search for a task."""

    tasks = load_tasks()

    if len(tasks) == 0:
        print("\nNo tasks available.")
        return

    keyword = input("\nEnter keyword to search: ").lower()

    found = False

    print("\n========== SEARCH RESULTS ==========\n")

    for i, task in enumerate(tasks, start=1):

        if keyword in task["task"].lower():

            status = "✅" if task["completed"] else "❌"

            print(f"{i}. {task['task']} {status}")

            found = True

    if not found:
        print("No matching tasks found.")

def show_statistics():
    """Display task statistics."""

    tasks = load_tasks()

    total = len(tasks)
    completed = 0

    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed

    print("\n========== TASK STATISTICS ==========")
    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")