"""Todo service for managing tasks in memory."""

from typing import List, Optional
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from models import Task


class TodoServiceError(Exception):
    """Base exception for todo service errors."""
    pass


class TaskNotFoundError(TodoServiceError):
    """Raised when a task ID is not found."""
    pass


class TodoService:
    """Manages task operations in memory.

    Provides CRUD operations for tasks with auto-incrementing IDs.
    All data is stored in memory and lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize the todo service with empty task list."""
        self._tasks: List[Task] = []
        self._next_id: int = 1
        self._available_ids: List[int] = []  # Pool of reusable IDs (min-heap)

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID.

        Args:
            task_id: The unique ID of the task to retrieve.

        Returns:
            The Task if found, None otherwise.
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Create a new task with auto-generated ID.

        Reuses smallest available ID if any deleted, otherwise uses next_id.

        Args:
            title: The task title (required, non-empty).
            description: Optional detailed description.

        Returns:
            The newly created Task.

        Raises:
            TodoServiceError: If title is empty.
        """
        if not title or not title.strip():
            raise TodoServiceError("Title cannot be empty.")

        # Reuse smallest available ID, or get next new ID
        if self._available_ids:
            task_id = self._available_ids.pop(0)  # Get smallest available
        else:
            task_id = self._next_id
            self._next_id += 1

        task = Task(
            id=task_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False,
        )
        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks.

        Returns:
            List of all tasks in insertion order.
        """
        return self._tasks.copy()

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ) -> bool:
        """Update task title and/or description.

        Args:
            task_id: The ID of the task to update.
            title: New title (optional - keeps original if not provided).
            description: New description (optional - keeps original if not provided).

        Returns:
            True if task was updated, False if not found.

        Raises:
            TodoServiceError: If title is provided but empty.
        """
        if title is not None and not title.strip():
            raise TodoServiceError("Title cannot be empty.")

        task = self.get_task(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title.strip()
        if description is not None:
            task.description = description.strip() if description.strip() else None

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Adds the deleted ID to the pool for reuse.

        Args:
            task_id: The ID of the task to delete.

        Returns:
            True if task was deleted, False if not found.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                self._available_ids.append(task_id)  # Reuse this ID later
                self._available_ids.sort()  # Keep smallest first
                return True
        return False

    def toggle_complete(self, task_id: int) -> bool:
        """Toggle task completion status.

        Args:
            task_id: The ID of the task to toggle.

        Returns:
            True if task was toggled, False if not found.
        """
        task = self.get_task(task_id)
        if task is None:
            return False
        task.completed = not task.completed
        return True
