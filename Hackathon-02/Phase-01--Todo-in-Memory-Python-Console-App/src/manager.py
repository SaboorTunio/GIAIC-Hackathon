"""
Todo manager for handling task operations.
"""
from typing import List, Optional
from models import Task


class TodoManager:
    """
    Manages todo tasks in memory using an in-memory list.
    """
    def __init__(self):
        """
        Initialize the TodoManager with an empty task list and next ID counter.
        """
        self._tasks: List[Task] = []
        self._next_id = 1

    def _get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            The next available ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the task list.

        Args:
            title: The task title (required)
            description: Optional description of the task

        Returns:
            The newly created Task instance

        Raises:
            ValueError: If title is empty
        """
        task_id = self._get_next_id()
        task = Task(task_id, title, description, completed=False)
        self._tasks.append(task)
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task instance if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the task list.

        Returns:
            List of all Task instances
        """
        return self._tasks.copy()

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task's title or description.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip() if description else None

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was found and deleted, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self._tasks.remove(task)
        return True

    def toggle_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the task was found and toggled, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.completed = not task.completed
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID without incrementing the counter.
        Used for validation purposes.

        Returns:
            The next available ID
        """
        return self._next_id