# Task Manager Functions
# Author: Zandile Ngwamba
# Internship Task 3

from task_manager import (
    add_task,
    load_tasks,
    complete_task,
    delete_task,
    search_task,
    show_statistics
)

while True:

    print("\n" + "=" * 50)
    print("          TO-DO LIST MANAGER")
    print("=" * 50)

    print("\nWelcome to your Task Manager!\n")

    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Statistics")
    print("7. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        tasks = load_tasks()

        if len(tasks) == 0:
            print("\nNo tasks available.")

        else:
            print("\n========== YOUR TASKS ==========\n")

            for i, task in enumerate(tasks, start=1):

                status = "✅" if task["completed"] else "❌"

                print(f"{i}. {task['task']} {status}")

    elif choice == "2":

        add_task()

    elif choice == "3":

        complete_task()

    elif choice == "4":

        delete_task()

    elif choice == "5":

        search_task()

    elif choice == "6":

        show_statistics()

    elif choice == "7":

        print("\nThank you for using the Task Manager!")
        print("Goodbye 👋")
        break

    else:

        print("\n❌ Invalid option. Please try again.")