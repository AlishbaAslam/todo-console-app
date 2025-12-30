"""Console interface for the todo application."""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from todo_service import TodoService, TodoServiceError


# ANSI color codes
class Colors:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright foreground colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


def colorize(text: str, color: str) -> str:
    """Apply color to text.

    Args:
        text: The text to colorize.
        color: ANSI color code.

    Returns:
        Colorized text with reset code.
    """
    return f"{color}{text}{Colors.RESET}"


def display_menu() -> None:
    """Display the main menu options."""
    print()
    print(colorize("=" * 40, Colors.BRIGHT_CYAN))
    print(colorize("    📝 TODO CONSOLE APP", Colors.BOLD + Colors.BRIGHT_YELLOW))
    print(colorize("=" * 40, Colors.BRIGHT_CYAN))
    print()
    print(colorize("  1. ➕ Add Task", Colors.CYAN))
    print(colorize("  2. 📋 View Tasks", Colors.CYAN))
    print(colorize("  3. ✏️  Update Task", Colors.CYAN))
    print(colorize("  4. 🗑️  Delete Task", Colors.CYAN))
    print(colorize("  5. ✅ Mark Complete", Colors.CYAN))
    print(colorize("  6. 🚪 Exit", Colors.BRIGHT_RED))
    print()
    print(colorize("-" * 40, Colors.DIM))


def get_menu_choice() -> int:
    """Get and validate menu choice from user.

    Returns:
        Valid menu choice (1-6).
    """
    while True:
        try:
            choice = int(input(colorize("Enter your choice (1-6): ", Colors.BRIGHT_GREEN)).strip())
            if 1 <= choice <= 6:
                return choice
            print(colorize("Error: Please enter a number between 1 and 6.", Colors.BRIGHT_RED))
        except ValueError:
            print(colorize("Error: Please enter a valid number.", Colors.BRIGHT_RED))


def get_task_input() -> tuple[str, str]:
    """Get task title and optional description from user.

    Returns:
        Tuple of (title, description).
    """
    while True:
        title = input(colorize("Enter title: ", Colors.BRIGHT_GREEN)).strip()
        if title:
            break
        print(colorize("Error: Title cannot be empty. Please try again.", Colors.BRIGHT_RED))

    description = input(colorize("Enter description (optional): ", Colors.BRIGHT_GREEN)).strip()
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
            task_id = int(input(colorize(prompt, Colors.BRIGHT_GREEN)).strip())
            if task_id > 0:
                return task_id
            print(colorize("Error: Please enter a positive number.", Colors.BRIGHT_RED))
        except ValueError:
            print(colorize("Error: Please enter a valid number.", Colors.BRIGHT_RED))


def run_add_task(service: TodoService) -> None:
    """Run the Add Task workflow.

    Args:
        service: The TodoService instance.
    """
    print()
    print(colorize("➕ Add Task", Colors.BOLD + Colors.CYAN))
    print(colorize("-" * 20, Colors.DIM))

    title, description = get_task_input()

    try:
        task = service.add_task(title, description)
        print(colorize(f"✅ Task added successfully! (ID: {task.id})", Colors.BRIGHT_GREEN))
    except TodoServiceError as e:
        print(colorize(f"Error: {e}", Colors.BRIGHT_RED))


def run_view_tasks(service: TodoService) -> None:
    """Run the View Tasks workflow.

    Args:
        service: The TodoService instance.
    """
    print()
    print(colorize("📋 Your Tasks", Colors.BOLD + Colors.CYAN))
    print(colorize("-" * 20, Colors.DIM))

    tasks = service.get_all_tasks()

    if not tasks:
        print(colorize("No tasks yet. Add one to get started! 📝", Colors.DIM))
        return

    for task in tasks:
        status_emoji = "✅" if task.completed else "⬜"
        status_color = Colors.BRIGHT_GREEN if task.completed else Colors.DIM
        status_text = colorize(f"[{status_emoji}]", status_color)
        title_color = Colors.WHITE if task.completed else Colors.BRIGHT_WHITE
        title_text = colorize(task.title, title_color)
        print(f"{status_text} {colorize(f'{task.id}.', Colors.YELLOW)} {title_text}")
        if task.description:
            print(colorize(f"    {task.description}", Colors.DIM))


def run_update_task(service: TodoService) -> None:
    """Run the Update Task workflow.

    Args:
        service: The TodoService instance.
    """
    print()
    print(colorize("✏️  Update Task", Colors.BOLD + Colors.CYAN))
    print(colorize("-" * 20, Colors.DIM))

    task_id = get_task_id("Enter task ID to update: ")
    task = service.get_task(task_id)

    if task is None:
        print(colorize(f"Error: Task with ID {task_id} not found.", Colors.BRIGHT_RED))
        return

    print(colorize(f"Current title: {task.title}", Colors.DIM))
    new_title = input(colorize("Enter new title (leave empty to keep): ", Colors.BRIGHT_GREEN)).strip()
    if not new_title:
        new_title = task.title

    print(colorize(f"Current description: {task.description or '(none)'}", Colors.DIM))
    new_desc = input(colorize("Enter new description (leave empty to keep): ", Colors.BRIGHT_GREEN)).strip()
    if not new_desc:
        new_desc = task.description

    if service.update_task(task_id, title=new_title, description=new_desc):
        print(colorize("✅ Task updated successfully!", Colors.BRIGHT_GREEN))
    else:
        print(colorize("Error: Failed to update task.", Colors.BRIGHT_RED))


def run_delete_task(service: TodoService) -> None:
    """Run the Delete Task workflow.

    Args:
        service: The TodoService instance.
    """
    print()
    print(colorize("🗑️  Delete Task", Colors.BOLD + Colors.CYAN))
    print(colorize("-" * 20, Colors.DIM))

    task_id = get_task_id("Enter task ID to delete: ")

    if service.delete_task(task_id):
        print(colorize("🗑️  Task deleted successfully!", Colors.BRIGHT_GREEN))
    else:
        print(colorize(f"Error: Task with ID {task_id} not found.", Colors.BRIGHT_RED))


def run_mark_complete(service: TodoService) -> None:
    """Run the Mark Complete workflow.

    Args:
        service: The TodoService instance.
    """
    print()
    print(colorize("✅ Mark Complete", Colors.BOLD + Colors.CYAN))
    print(colorize("-" * 20, Colors.DIM))

    task_id = get_task_id("Enter task ID to mark complete: ")

    if service.toggle_complete(task_id):
        task = service.get_task(task_id)
        status = "complete" if task.completed else "incomplete"
        emoji = "✅" if task.completed else "⬜"
        color = Colors.BRIGHT_GREEN if task.completed else Colors.YELLOW
        print(colorize(f"{emoji} Task {task_id} is now {status}.", color))
    else:
        print(colorize(f"Error: Task with ID {task_id} not found.", Colors.BRIGHT_RED))


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
            print()
            print(colorize("Goodbye! Thanks for using Todo Console App 👋", Colors.BRIGHT_YELLOW))
            sys.exit(0)
