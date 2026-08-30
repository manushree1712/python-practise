tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add task
    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Delete task
    elif choice == "3":
        if len(tasks) == 0:
            print("There are no tasks to delete!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Deleted: {deleted_task}")
            else:
                print("Invalid task number!")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice!")