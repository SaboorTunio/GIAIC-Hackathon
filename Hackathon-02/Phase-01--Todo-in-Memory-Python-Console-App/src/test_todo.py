"""
Unit tests for the Todo CLI application.
"""
import unittest
import sys
import os

# Add the src directory to the path so we can import the modules
sys.path.insert(0, os.path.dirname(__file__))

from models import Task
from manager import TodoManager


class TestTask(unittest.TestCase):
    """Test cases for the Task class."""

    def test_create_task_with_title_and_description(self):
        """Test creating a task with title and description."""
        task = Task(1, "Test title", "Test description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)

    def test_create_task_without_description(self):
        """Test creating a task without description."""
        task = Task(1, "Test title")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertIsNone(task.description)
        self.assertFalse(task.completed)

    def test_create_completed_task(self):
        """Test creating a completed task."""
        task = Task(1, "Test title", "Test description", completed=True)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "Test description")
        self.assertTrue(task.completed)

    def test_empty_title_raises_error(self):
        """Test that creating a task with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            Task(1, "")

    def test_whitespace_only_title_raises_error(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            Task(1, "   ")

    def test_title_stripped_of_whitespace(self):
        """Test that title is stripped of leading/trailing whitespace."""
        task = Task(1, "  Test title  ", "  Test description  ")
        self.assertEqual(task.title, "Test title")
        self.assertEqual(task.description, "Test description")


class TestTodoManager(unittest.TestCase):
    """Test cases for the TodoManager class."""

    def setUp(self):
        """Set up a fresh TodoManager for each test."""
        self.manager = TodoManager()

    def test_initial_state(self):
        """Test initial state of TodoManager."""
        self.assertEqual(len(self.manager.get_all_tasks()), 0)
        self.assertEqual(self.manager.get_next_id(), 1)

    def test_add_task(self):
        """Test adding a task."""
        task = self.manager.add_task("Test task", "Test description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)

        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 1)

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks with auto-incrementing IDs."""
        task1 = self.manager.add_task("Task 1")
        task2 = self.manager.add_task("Task 2")
        task3 = self.manager.add_task("Task 3")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 3)

    def test_get_task_by_id(self):
        """Test retrieving a task by its ID."""
        task = self.manager.add_task("Test task", "Test description")
        retrieved_task = self.manager.get_task_by_id(1)

        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.id, 1)
        self.assertEqual(retrieved_task.title, "Test task")
        self.assertEqual(retrieved_task.description, "Test description")

    def test_get_nonexistent_task(self):
        """Test retrieving a task that doesn't exist."""
        result = self.manager.get_task_by_id(999)
        self.assertIsNone(result)

    def test_update_task_title(self):
        """Test updating a task's title."""
        task = self.manager.add_task("Original title", "Original description")
        success = self.manager.update_task(1, title="New title")

        self.assertTrue(success)
        updated_task = self.manager.get_task_by_id(1)
        self.assertEqual(updated_task.title, "New title")
        self.assertEqual(updated_task.description, "Original description")

    def test_update_task_description(self):
        """Test updating a task's description."""
        task = self.manager.add_task("Test title", "Original description")
        success = self.manager.update_task(1, description="New description")

        self.assertTrue(success)
        updated_task = self.manager.get_task_by_id(1)
        self.assertEqual(updated_task.title, "Test title")
        self.assertEqual(updated_task.description, "New description")

    def test_update_task_both_fields(self):
        """Test updating both title and description."""
        task = self.manager.add_task("Original title", "Original description")
        success = self.manager.update_task(1, title="New title", description="New description")

        self.assertTrue(success)
        updated_task = self.manager.get_task_by_id(1)
        self.assertEqual(updated_task.title, "New title")
        self.assertEqual(updated_task.description, "New description")

    def test_update_nonexistent_task(self):
        """Test updating a task that doesn't exist."""
        success = self.manager.update_task(999, title="New title")
        self.assertFalse(success)

    def test_update_task_with_empty_title(self):
        """Test updating a task with empty title raises ValueError."""
        task = self.manager.add_task("Test title")
        with self.assertRaises(ValueError):
            self.manager.update_task(1, title="")

    def test_delete_task(self):
        """Test deleting a task."""
        task = self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.get_all_tasks()), 1)

        success = self.manager.delete_task(1)
        self.assertTrue(success)
        self.assertEqual(len(self.manager.get_all_tasks()), 0)

    def test_delete_nonexistent_task(self):
        """Test deleting a task that doesn't exist."""
        success = self.manager.delete_task(999)
        self.assertFalse(success)

    def test_toggle_completion(self):
        """Test toggling task completion status."""
        task = self.manager.add_task("Test task")
        self.assertFalse(task.completed)

        # Toggle to completed
        success = self.manager.toggle_completion(1)
        self.assertTrue(success)
        self.assertTrue(self.manager.get_task_by_id(1).completed)

        # Toggle back to incomplete
        success = self.manager.toggle_completion(1)
        self.assertTrue(success)
        self.assertFalse(self.manager.get_task_by_id(1).completed)

    def test_toggle_nonexistent_task(self):
        """Test toggling completion for a task that doesn't exist."""
        success = self.manager.toggle_completion(999)
        self.assertFalse(success)


if __name__ == '__main__':
    unittest.main()