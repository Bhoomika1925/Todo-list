# to_do_list.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

while True:
    print("\nTo-Do List Options:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
