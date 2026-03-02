# main.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {
            "id": len(self.tasks) + 1,
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
            print(f"{idx}. [{status}] {task['title']} (id: {task['id']})")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            print(f"Task '{self.tasks[index - 1]['title']}' marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed = self.tasks.pop(index - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")

def main():
    manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                manager.add_task(title)
                print("Task added.")
            else:
                print("Task title cannot be empty.")
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.list_tasks()
            try:
                idx = int(input("Enter task number to complete: "))
                manager.complete_task(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            manager.list_tasks()
            try:
                idx = int(input("Enter task number to delete: "))
                manager.delete_task(idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()