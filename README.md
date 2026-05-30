# task-tracker-cli
A command-line task tracker built in Python
. It Supports adding, completing, deleting, and searching tasks with persistent JSON storage

##Features 
-Add tasks with auto incrementing IDs 
-Mark task as complete
-delete tasks
-search tasks by keyword
-filter by status (pending/completed)
-Persistent storage - tasks survive across program runs 
-Input validation - handles bad input gracefully

## Installation

'''bash
git clone https://github.com/syedwajiulhassan715-rgb/task-tracker-cli
cd task-tracker-cli
python task_tracker.py list
'''

## Usage
```bash
# Add a task
python task_tracker.py add "Learn Python"

# List all tasks
python task_tracker.py list

# Complete a task
python task_tracker.py complete 1

# Delete a task
python task_tracker.py delete 1

# Search tasks
python task_tracker.py search "python"
```

## What I Learned from Building This

- Python fundamentals: dicts, lists, file I/O, error handling
- JSON persistence — saving and loading application state
- Input validation — rejecting bad input before it causes problems
- argparse — building real command-line interfaces
- Code refactoring — extracting helper functions (get_task_by_id)
- The mutable default argument trap and how to avoid it

## Tech Stack

- Python 3.11+
- No external dependencies