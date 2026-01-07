"""
Simple test script for the Todo CLI application.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.models import Task
from src.manager import TodoManager


def test_task_creation():
    """Test creating tasks."""
    print("Testing Task creation...")

    # Test basic task creation
    task = Task(1, "Test title", "Test description")
    assert task.id == 1
    assert task.title == "Test title"
    assert task.description == "Test description"
    assert task.completed == False
    print("PASS: Basic task creation works")

    # Test task without description
    task2 = Task(2, "Test title 2")
    assert task2.id == 2
    assert task2.title == "Test title 2"
    assert task2.description is None
    print("PASS: Task without description works")

    # Test completed task
    task3 = Task(3, "Test title 3", "Test description 3", completed=True)
    assert task3.completed == True
    print("PASS: Completed task works")

    # Test empty title raises error
    try:
        Task(4, "")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("PASS: Empty title validation works")

    print("All Task tests passed!\n")


def test_todo_manager():
    """Test TodoManager functionality."""
    print("Testing TodoManager...")

    manager = TodoManager()

    # Test initial state
    assert len(manager.get_all_tasks()) == 0
    assert manager.get_next_id() == 1
    print("PASS: Initial state is correct")

    # Test adding tasks
    task1 = manager.add_task("Task 1", "Description 1")
    task2 = manager.add_task("Task 2")

    assert task1.id == 1
    assert task2.id == 2
    assert len(manager.get_all_tasks()) == 2
    print("PASS: Adding tasks works")

    # Test retrieving tasks
    retrieved_task = manager.get_task_by_id(1)
    assert retrieved_task is not None
    assert retrieved_task.title == "Task 1"
    assert retrieved_task.description == "Description 1"
    print("PASS: Retrieving tasks works")

    # Test updating tasks
    success = manager.update_task(1, title="Updated Task 1", description="Updated Description")
    assert success == True
    updated_task = manager.get_task_by_id(1)
    assert updated_task.title == "Updated Task 1"
    assert updated_task.description == "Updated Description"
    print("PASS: Updating tasks works")

    # Test toggling completion
    task3 = manager.add_task("Task 3")
    assert task3.completed == False
    success = manager.toggle_completion(3)
    assert success == True
    toggled_task = manager.get_task_by_id(3)
    assert toggled_task.completed == True
    print("PASS: Toggling completion works")

    # Test deleting tasks
    initial_count = len(manager.get_all_tasks())
    success = manager.delete_task(1)
    assert success == True
    assert len(manager.get_all_tasks()) == initial_count - 1
    assert manager.get_task_by_id(1) is None
    print("PASS: Deleting tasks works")

    print("All TodoManager tests passed!\n")


def test_cli_interaction():
    """Test basic CLI functionality by simulating commands."""
    print("Testing CLI functionality...")

    from src.main import parse_command, handle_add_command, handle_view_command, handle_update_command, handle_delete_command, handle_complete_command

    manager = TodoManager()

    # Test command parsing
    command, args = parse_command("add My Task Title")
    assert command == "add"
    assert args == ["My", "Task", "Title"]
    print("PASS: Command parsing works")

    # Test add command
    result = handle_add_command(manager, ["New", "Task"])
    assert result == True
    assert len(manager.get_all_tasks()) == 1
    print("PASS: Add command handler works")

    # Test view command
    result = handle_view_command(manager)
    assert result == True
    print("PASS: View command handler works")

    print("All CLI tests passed!\n")


if __name__ == "__main__":
    print("Running Todo Application Tests...\n")

    test_task_creation()
    test_todo_manager()
    test_cli_interaction()

    print("SUCCESS: All tests passed successfully!")