import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [task.strip() for task in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n🟡 No tasks found.\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!\n")
    else:
        print("❌ Cannot add empty task.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed}' deleted!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

def menu():
    tasks = load_tasks()
    while True:
        print("=== To-Do List Menu ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting. Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
