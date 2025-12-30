"""Console interface for the todo application."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from todo_service import TodoService, TodoServiceError


def display_menu() -> None:
    """Display the main menu options."""
    print()
    print("=" * 40)
    print("      TODO CONSOLE APP v1.0")
    print("=" * 40)
    print()
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Update Task")
    print("  4. Delete Task")
    print("  5. Mark Complete")
    print("  6. Exit")
    print()
    print("-" * 40)


def get_menu_choice() -> int:
    """Get and validate menu choice from user.

    Returns:
        Valid menu choice (1-6).
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-6): ").strip())
            if 1 <= choice <= 6:
                return choice
            print("Error: Please enter a number between 1 and 6.")
        except ValueError:
            print("Error: Please enter a valid number.")


def get_task_input() -> tuple[str, str]:
    """Get task title and optional description from user.

    Returns:
        Tuple of (title, description).
    """
    while True:
        title = input("Enter title: ").strip()
        if title:
            break
        print("Error: Title cannot be empty. Please try again.")

    description = input("Enter description (optional): ").strip()
    return title, description


def get_task_id(prompt: str) -> int:
    """Get and validate a task ID from user.

    Args:
        prompt: The prompt to display.

    Returns:
        Valid positive integer.
    """
    while True:
        try:
            task_id = int(input(prompt).strip())
            if task_id > 0:
                return task_id
            print("Error: Please enter a positive number.")
        except ValueError:
            print("Error: Please enter a valid number.")


def run_add_task(service: TodoService) -> None:
    """Run the Add Task workflow.

    Args:
        service: The TodoService instance.
    """
    print("\nAdd Task")
    print("-" * 20)

    title, description = get_task_input()

    try:
        task = service.add_task(title, description)
        print(f"Task added successfully! (ID: {task.id})")
    except TodoServiceError as e:
        print(f"Error: {e}")


def run_view_tasks(service: TodoService) -> None:
    """Run the View Tasks workflow.

    Args:
        service: The TodoService instance.
    """
    print("\nYour Tasks")
    print("-" * 20)

    tasks = service.get_all_tasks()

    if not tasks:
        print("No tasks yet. Add one to get started!")
        return

    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"{status} {task.id}. {task.title}")
        if task.description:
            print(f"    {task.description}")


def run_update_task(service: TodoService) -> None:
    """Run the Update Task workflow.

    Args:
        service: The TodoService instance.
    """
    print("\nUpdate Task")
    print("-" * 20)

    task_id = get_task_id("Enter task ID to update: ")
    task = service.get_task(task_id)

    if task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    print(f"Current title: {task.title}")
    new_title = input("Enter new title (leave empty to keep): ").strip()
    if not new_title:
        new_title = task.title

    print(f"Current description: {task.description or '(none)'}")
    new_desc = input("Enter new description (leave empty to keep): ").strip()
    if not new_desc:
        new_desc = task.description

    if service.update_task(task_id, title=new_title, description=new_desc):
        print("Task updated successfully!")
    else:
        print("Error: Failed to update task.")


def run_delete_task(service: TodoService) -> None:
    """Run the Delete Task workflow.

    Args:
        service: The TodoService instance.
    """
    print("\nDelete Task")
    print("-" * 20)

    task_id = get_task_id("Enter task ID to delete: ")

    if service.delete_task(task_id):
        print("Task deleted successfully!")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def run_mark_complete(service: TodoService) -> None:
    """Run the Mark Complete workflow.

    Args:
        service: The TodoService instance.
    """
    print("\nMark Complete")
    print("-" * 20)

    task_id = get_task_id("Enter task ID to mark complete: ")

    if service.toggle_complete(task_id):
        task = service.get_task(task_id)
        status = "complete" if task.completed else "incomplete"
        print(f"Task {task_id} is now {status}.")
    else:
        print(f"Error: Task with ID {task_id} not found.")


def run_cli() -> None:
    """Run the main CLI loop."""
    service = TodoService()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            run_add_task(service)
        elif choice == 2:
            run_view_tasks(service)
        elif choice == 3:
            run_update_task(service)
        elif choice == 4:
            run_delete_task(service)
        elif choice == 5:
            run_mark_complete(service)
        elif choice == 6:
            print("\nGoodbye!")
            sys.exit(0)
