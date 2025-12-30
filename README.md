# Todo Console App

A simple in-memory todo console application built with Python 3.13+.

## Features

- **Add Task** - Create tasks with title and optional description
- **View Tasks** - See all tasks with their completion status
- **Update Task** - Modify task title and/or description
- **Delete Task** - Remove tasks by ID
- **Mark Complete** - Toggle task completion status

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

When you run the application, you'll see a menu:

```
========================================
      TODO CONSOLE APP v1.0
========================================

  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete
  6. Exit

----------------------------------------
Enter your choice (1-6):
```

### Example Session

```
Enter your choice (1-6): 1

Add Task
--------------------
Enter title: Buy groceries
Enter description (optional): Milk, eggs, bread
Task added successfully! (ID: 1)

Enter your choice (1-6): 2

Your Tasks
--------------------
[ ] 1. Buy groceries
    Milk, eggs, bread

Enter your choice (1-6): 5

Mark Complete
--------------------
Enter task ID to mark complete: 1
Task 1 is now complete.

Enter your choice (1-6): 2

Your Tasks
--------------------
[X] 1. Buy groceries
    Milk, eggs, bread

Enter your choice (1-6): 6

Goodbye!
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
