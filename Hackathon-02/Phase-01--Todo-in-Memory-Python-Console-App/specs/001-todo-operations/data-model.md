# Data Model: Basic Todo Operations

## Entities

### Task
- **id**: Integer (required) - Unique identifier for the task, auto-incrementing
- **title**: String (required) - The task title/description
- **description**: String (optional) - Additional details about the task
- **completed**: Boolean (required) - Whether the task is completed, defaults to False

### Task List
- **tasks**: Array/List of Task entities
- Maintains order of insertion
- Provides methods for CRUD operations

## Validation Rules
- Task.title is required and must not be empty
- Task.id must be unique within the Task List
- Task.completed defaults to False when creating new tasks
- Task.description can be empty or null

## State Transitions
- New Task: created with completed=False
- Completed Task: toggled from completed=False to completed=True
- Reopened Task: toggled from completed=True to completed=False
- Deleted Task: removed from Task List

## Example Structure
```python
{
    'id': 1,
    'title': 'Sample task',
    'description': 'Additional details about the task',
    'completed': False
}
```

## In-Memory Storage
- All data stored in Python dictionaries and lists
- No persistent storage - data resets on application restart
- Stored in TodoManager class instance variables