import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def get_current_time():
    return datetime.now().isoformat(timespec="seconds")


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def add_task(description):
    tasks = load_tasks()

    new_task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": get_current_time(),
        "updatedAt": get_current_time()
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_task['id']})")


def list_tasks(status_filter=None):
    tasks = load_tasks()

    if status_filter:
        tasks = [task for task in tasks if task["status"] == status_filter]

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(
            f"[{task['id']}] {task['description']} "
            f"- {task['status']} "
            f"(Created: {task['createdAt']}, Updated: {task['updatedAt']})"
        )


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id, new_description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    task["description"] = new_description
    task["updatedAt"] = get_current_time()

    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")


def delete_task(task_id):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    tasks.remove(task)
    save_tasks(tasks)

    print(f"Task {task_id} deleted successfully.")


def mark_task(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    task["status"] = status
    task["updatedAt"] = get_current_time()

    save_tasks(tasks)
    print(f"Task {task_id} marked as {status}.")


def show_help():
    print("""
Task Tracker CLI

Usage:
  python task_cli.py add "Task description"
  python task_cli.py update <id> "New description"
  python task_cli.py delete <id>
  python task_cli.py mark-in-progress <id>
  python task_cli.py mark-done <id>
  python task_cli.py list
  python task_cli.py list done
  python task_cli.py list todo
  python task_cli.py list in-progress
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            return
        add_task(sys.argv[2])

    elif command == "list":
        valid_statuses = ["todo", "in-progress", "done"]

        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3 and sys.argv[2] in valid_statuses:
            list_tasks(sys.argv[2])
        else:
            print("Error: Invalid status. Use todo, in-progress, or done.")

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Usage: python task_cli.py update <id> \"New description\"")
            return

        try:
            task_id = int(sys.argv[2])
            update_task(task_id, sys.argv[3])
        except ValueError:
            print("Error: Task ID must be a number.")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Usage: python task_cli.py delete <id>")
            return

        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: Usage: python task_cli.py mark-in-progress <id>")
            return

        try:
            task_id = int(sys.argv[2])
            mark_task(task_id, "in-progress")
        except ValueError:
            print("Error: Task ID must be a number.")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: Usage: python task_cli.py mark-done <id>")
            return

        try:
            task_id = int(sys.argv[2])
            mark_task(task_id, "done")
        except ValueError:
            print("Error: Task ID must be a number.")

    else:
        print(f"Error: Unknown command '{command}'.")
        show_help()


if __name__ == "__main__":
    main()