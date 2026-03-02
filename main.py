
# main.py
import json
import os
from typing import List, Dict, Optional

class TaskManager:
    def __init__(self, filepath: str = "tasks.json"):
        self.tasks: List[Dict] = []
        self.filepath = filepath
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from JSON file if it exists."""
        try:
            if os.path.exists(self.filepath):
                with open(self.filepath, 'r') as f:
                    self.tasks = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load tasks - {e}")
            self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to JSON file."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error: Could not save tasks - {e}")

    def add_task(self, title: str) -> bool:
        """Add a new task and save to file."""
        if not title or not title.strip():
            return False
        task = {
            "id": len(self.tasks) + 1,
            "title": title.strip(),
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        return True

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. [{status}] {task['title']} (id: {task['id']})")

    def complete_task(self, index: int) -> bool:
        """Mark a task as complete and save to file."""
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            self.save_tasks()
            return True
        return False

    def delete_task(self, index: int) -> bool:
        """Delete a task and save to file."""
        if 1 <= index <= len(self.tasks):
            self.tasks.pop(index - 1)
            self.save_tasks()
            return True
        return False

    def search_tasks(self, keyword: str) -> List[Dict]:
        """Search tasks by keyword."""
        keyword = keyword.lower()
        return [task for task in self.tasks if keyword in task['title'].lower()]

def main():
    manager = TaskManager()

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")

        choice = input("\nSelect option: ").strip()

        try:
            if choice == "1":
                title = input("Enter task title: ").strip()
                if manager.add_task(title):
                    print("✓ Task added successfully.")
                else:
                    print("✗ Task title cannot be empty.")
            elif choice == "2":
                manager.list_tasks()
            elif choice == "3":
                manager.list_tasks()
                if manager.tasks:
                    idx = int(input("Enter task number to complete: ").strip())
                    if manager.complete_task(idx):
                        print(f"✓ Task marked as complete.")
                    else:
                        print("✗ Invalid task number.")
            elif choice == "4":
                manager.list_tasks()
                if manager.tasks:
                    idx = int(input("Enter task number to delete: ").strip())
                    if manager.delete_task(idx):
                        print("✓ Task deleted.")
                    else:
                        print("✗ Invalid task number.")
            elif choice == "5":
                keyword = input("Enter search keyword: ").strip()
                results = manager.search_tasks(keyword)
                if results:
                    print(f"\nFound {len(results)} task(s):")
                    for idx, task in enumerate(results, start=1):
                        status = "✓" if task["completed"] else "✗"
                        print(f"{idx}. [{status}] {task['title']}")
                else:
                    print("No tasks found matching that keyword.")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("✗ Invalid option. Please try again.")
        except ValueError:
            print("✗ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()