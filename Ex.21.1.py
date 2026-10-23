# Project Task Board

tasks = []

n = int(input("Enter the number of tasks: "))

for i in range(n):
    name = input(f"Enter task {i + 1} name: ")
    status = input("Enter status (Pending/In Progress/Completed): ")

    tasks.append({"name": name, "status": status})

while True:
    print("\n===== PROJECT TASK BOARD =====")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']} - {task['status']}")

    choice = input("\nEnter task number to update (0 to exit): ")

    if choice == "0":
        break

    try:
        index = int(choice) - 1

        if 0 <= index < len(tasks):
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")

            status_choice = input("Select new status: ")

            statuses = {
                "1": "Pending",
                "2": "In Progress",
                "3": "Completed"
            }

            if status_choice in statuses:
                tasks[index]["status"] = statuses[status_choice]
                print("Task updated successfully!")
            else:
                print("Invalid status choice.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

print("\nFinal Task Summary")

for task in tasks:
    print(f"{task['name']} - {task['status']}")
