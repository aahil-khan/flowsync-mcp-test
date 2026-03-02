# main.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {
            "title": title,
            "completed": False
        }
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['title']}")

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
            print("Task added.")
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()