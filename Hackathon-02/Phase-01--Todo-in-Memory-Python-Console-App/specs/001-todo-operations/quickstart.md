# Quickstart Guide: Basic Todo Operations

## Installation
1. Ensure Python 3.13+ is installed on your system
2. Install dependencies using UV package manager:
   ```
   uv pip install -r requirements.txt
   ```
   Or if no requirements.txt exists yet:
   ```
   # No external dependencies required - pure Python
   ```

## Usage
1. Navigate to the project directory
2. Run the application:
   ```
   python src/main.py
   ```
3. The interactive CLI will start and display a menu of available commands
4. Follow the prompts to add, view, update, complete, or delete tasks
5. Type "exit" to quit the application

## Available Commands
- `add` - Add a new task with title and optional description
- `view` - Display all tasks with their ID, status, title, and description
- `update` - Modify the title or description of an existing task
- `delete` - Remove a task by its ID
- `complete` - Toggle the completion status of a task
- `exit` - Quit the application

## Example Workflow
1. Start the application: `python src/main.py`
2. Add a task: `add "Buy groceries" "Milk, bread, eggs"`
3. View all tasks: `view`
4. Mark task as complete: `complete 1`
5. Update a task: `update 1 "Buy groceries" "Milk, bread, eggs, fruits"`
6. Exit: `exit`

## Configuration
No configuration required - the application runs with default settings and stores data in memory only.