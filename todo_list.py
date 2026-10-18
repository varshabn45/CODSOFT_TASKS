tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add a task")
    print("2. view tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task":task,"completed":False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks added!")
        else:
            for i, task in enumerate(tasks,start=1):
                status = "Completed" if task["completed"] else "pending"
                print(f"{i}. {task['task']}- {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks added!")
        else:
            for i, task in enumerate(tasks,start=1):
                print(f"{i}.{task['task']}")
            try:
                number = int(input("Enter task number to complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number-1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("invalid task number!")
            except ValueError:
                print("please enter a valid number!")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks,start=1):
                print(f"{i}. {task['task']}")
            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number-1)
                    print(f"Deleted task: {removed['task']}")
                else:
                    print("invalid task number!")
            except ValueError:
                print("please enter a valid number!")

    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")
