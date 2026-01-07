"""
Main entry point for the Todo CLI application with improved UX.
"""
import sys
from typing import List
from manager import TodoManager


def display_menu():
    """
    Display the clean menu options to the user.
    """
    print("\n" + "="*50)
    print("TODO CLI APPLICATION")
    print("="*50)
    print("What would you like to do?")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Toggle Complete")
    print("5. Delete Task")
    print("6. Exit")
    print("="*50)


def print_tasks_table(todo_manager: TodoManager):
    """
    Print tasks in a formatted table with headers (ID | Status | Title).

    Args:
        todo_manager: Instance of TodoManager
    """
    tasks = todo_manager.get_all_tasks()

    if not tasks:
        print("\nYour list is empty. Choose option 1 to add a task!")
        return

    print("\n" + "-" * 60)
    print(f"{'ID':<5} {'Status':<8} {'Title'}")
    print("-" * 60)

    for task in tasks:
        status = '[x]' if task.completed else '[ ]'
        print(f"{task.id:<5} {status:<8} {task.title}")

    print("-" * 60)


def get_task_id_input(prompt: str = "Enter task ID: ") -> int:
    """
    Get a task ID from user input with error handling.

    Args:
        prompt: The prompt to display to the user

    Returns:
        The task ID as an integer, or None if invalid input
    """
    try:
        task_id = int(input(prompt).strip())
        return task_id
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return None


def handle_add_task(todo_manager: TodoManager):
    """
    Handle adding a new task with improved UX.

    Args:
        todo_manager: Instance of TodoManager

    Returns:
        True if successful, False otherwise
    """
    title = input("Enter task title: ").strip()
    if not title:
        print("⚠️ Task title cannot be empty.")
        return False

    description = input("Enter task description (optional, press Enter to skip): ").strip()
    if not description:
        description = None

    try:
        task = todo_manager.add_task(title, description)
        print("✅ Task added successfully.")
        return True
    except ValueError as e:
        print(f"⚠️ {e}")
        return False


def handle_view_tasks(todo_manager: TodoManager):
    """
    Handle viewing all tasks with improved UX.

    Args:
        todo_manager: Instance of TodoManager
    """
    print_tasks_table(todo_manager)


def handle_update_task(todo_manager: TodoManager):
    """
    Handle updating a task with improved UX.

    Args:
        todo_manager: Instance of TodoManager

    Returns:
        True if successful, False otherwise
    """
    task_id = get_task_id_input("Enter task ID to update: ")
    if task_id is None:
        return False

    task = todo_manager.get_task_by_id(task_id)
    if not task:
        print(f"⚠️ Task with ID {task_id} not found.")
        return False

    print(f"Current title: {task.title}")
    new_title = input("Enter new title (press Enter to keep current): ").strip()

    print(f"Current description: {task.description or 'None'}")
    new_description = input("Enter new description (press Enter to keep current): ").strip()

    # If user pressed Enter without typing anything, keep the current value
    if not new_title:
        new_title = None
    if not new_description:
        new_description = None

    # If both are empty strings (user wants to clear description), set to None
    if new_description == "":
        new_description = None

    try:
        success = todo_manager.update_task(task_id,
                                         title=new_title if new_title is not None else task.title,
                                         description=new_description)
        if success:
            print("✅ Task updated successfully.")
            return True
        else:
            print(f"⚠️ Failed to update task with ID {task_id}.")
            return False
    except ValueError as e:
        print(f"⚠️ {e}")
        return False


def handle_toggle_complete(todo_manager: TodoManager):
    """
    Handle toggling task completion status with improved UX.

    Args:
        todo_manager: Instance of TodoManager

    Returns:
        True if successful, False otherwise
    """
    task_id = get_task_id_input("Enter task ID to toggle: ")
    if task_id is None:
        return False

    success = todo_manager.toggle_completion(task_id)
    if success:
        task = todo_manager.get_task_by_id(task_id)
        status = "completed" if task.completed else "pending"
        print(f"✅ Task {task_id} marked as {status}.")
        return True
    else:
        print(f"⚠️ Task with ID {task_id} not found.")
        return False


def handle_delete_task(todo_manager: TodoManager):
    """
    Handle deleting a task with improved UX.

    Args:
        todo_manager: Instance of TodoManager

    Returns:
        True if successful, False otherwise
    """
    task_id = get_task_id_input("Enter task ID to delete: ")
    if task_id is None:
        return False

    success = todo_manager.delete_task(task_id)
    if success:
        print("✅ Task deleted successfully.")
        return True
    else:
        print(f"⚠️ Task with ID {task_id} not found.")
        return False


def main():
    """
    Main function to run the Todo CLI application with improved UX.
    """
    print("Welcome to the Todo CLI Application!")
    print("Your tasks are stored in memory and will reset when you exit.")

    todo_manager = TodoManager()

    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                handle_add_task(todo_manager)
            elif choice == '2':
                handle_view_tasks(todo_manager)
            elif choice == '3':
                handle_update_task(todo_manager)
            elif choice == '4':
                handle_toggle_complete(todo_manager)
            elif choice == '5':
                handle_delete_task(todo_manager)
            elif choice == '6':
                print("Thank you for using Todo CLI. Goodbye!")
                sys.exit(0)
            else:
                print("⚠️ Please enter a number between 1 and 6.")

        except KeyboardInterrupt:
            print("\n\nReceived interrupt signal. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()