"""
Data models for the Todo application.
"""
from typing import Optional


class Task:
    """
    Represents a todo task with ID, title, description, and completion status.
    """
    def __init__(self, task_id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id: Unique identifier for the task
            title: The task title (required)
            description: Optional description of the task
            completed: Whether the task is completed (defaults to False)
        """
        if not title.strip():
            raise ValueError("Title cannot be empty")

        self.id = task_id
        self.title = title.strip()
        self.description = description.strip() if description else None
        self.completed = completed

    def to_dict(self) -> dict:
        """
        Convert the Task instance to a dictionary representation.

        Returns:
            Dictionary representation of the task
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    def __repr__(self) -> str:
        """
        String representation of the Task instance.

        Returns:
            String representation of the task
        """
        status = '[x]' if self.completed else '[ ]'
        desc = f" - {self.description}" if self.description else ""
        return f"{status} [{self.id}] {self.title}{desc}"