"""Task data model for the todo console application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique identifier for the task (auto-assigned).
        title: Brief description of what needs to be done (required).
        description: Optional detailed notes about the task.
        completed: Whether the task has been completed (default False).
    """

    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
