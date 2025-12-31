# Todo Console App

A simple in-memory todo console application built with Python 3.13+.

## Features

- **Add Task** - Create tasks with title, description, priority, and tags
- **View Tasks** - See all tasks with full metadata (Priorities, Tags, Due Dates)
- **Update Task** - Modify specific fields using a dedicated sub-menu
- **Delete Task** - Remove tasks by ID
- **Mark Complete** - Toggle task completion status
- **Search & Filter** - Find tasks by keyword, status, priority, or tags
- **Sort View** - Reorder by due date, priority, or alphabetically
- **Intelligent Recurrence** - Automate routine tasks (Daily, Weekly, Monthly)
- **Precise Scheduling** - Set due times (HH:MM) and receive console alerts
- **Batch Rescheduling** - Quickly move backlog (overdue) tasks to Today
- **Colorful Interface** - Enhanced UX with ANSI colors, emojis, and imminent alerts

## Setup

This project uses [UV](https://github.com/astral-sh/uv) for dependency management.

### Install UV (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Initialize the project

```bash
uv sync
```

## Running the Application

```bash
uv run python -m src.main
```

Or alternatively:

```bash
cd src
python main.py
```

## Usage

When you run the application, you'll see a colorful menu with emojis:

```
========================================
    📝 TODO CONSOLE APP
========================================

  1. ➕ Add Task
  2. 📋 View Tasks
  3. ✏️  Update Task
  4. 🗑️  Delete Task
  5. ✅ Mark Complete
  6. 🚪 Exit

----------------------------------------
Enter your choice (1-6):
```

### Example: Recurring Task

```
Enter your choice (1-9): 1

➕ Add Task
--------------------
Enter title: Morning Yoga
Enter description (optional): 20 min session
Priority: [1] High, [2] Medium, [3] Low
Select priority (default: 2): 1
Enter tags (comma-separated, max 3): health, routine
Enter due date (YYYY-MM-DD, optional): 2024-01-01
Enter due time (HH:MM, 24h, optional): 07:00
Recurrence: [1] None, [2] Daily, [3] Weekly, [4] Monthly
Select recurrence (default: 1): 2
✅ Task added successfully! (ID: 1)

Enter your choice (1-9): 5
✅ Mark Complete
--------------------
Enter task ID to mark complete: 1
✅ Task 1 is now complete.

Enter your choice (1-9): 2
📋 Your Tasks
--------------------
[✅] 1. (High) Morning Yoga #health #routine 📅 2024-01-01 07:00 🔃 Daily
[⬜] 2. (High) Morning Yoga #health #routine 📅 2024-01-02 07:00 🔃 Daily
```

## Project Structure

```
todo-console-app/
├── src/
│   ├── __init__.py
│   ├── main.py          # Entry point
│   ├── models.py        # Task dataclass
│   ├── todo_service.py  # Business logic
│   └── cli.py           # Console interface
├── .specify/
│   ├── memory/
│   │   └── constitution.md
│   └── templates/
├── specs/               # Specification history
├── history/             # PHR records
├── pyproject.toml
└── README.md
```

## Requirements Met

- All 5 core features implemented
- In-memory storage (no files, no database)
- Input validation and error handling
- Clean, modular Python code
- PEP 8 compliant

## License

MIT
