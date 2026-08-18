# ===========================
# TO-DO LIST APPLICATION
# ===========================

tasks = []

def show_menu():
    print("\n==============================")
    print("      TO-DO LIST MENU")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")
    print("==============================")

while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Edit Task
    elif choice == "3":
        if len(tasks) == 0:
            print("Task list is empty.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter task number to edit: "))
                if 1 <= index <= len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[index - 1] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("Task list is empty.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter task number to delete: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"'{removed}' deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("Thank you for using the To-Do List Application.")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
