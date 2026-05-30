import json
import argparse


def save_tasks():
    """Save tasks and next available ID to file"""
    data = {"tasks": tasks, "next_id": next_id}
    with open("tasks.json", "w") as f:
        json.dump(data, f)


def load_tasks():
    """Load saved tasks; start fresh if file doesn't exist"""
    try:
        with open("tasks.json", "r") as f:
            data = json.load(f)
            return (data["tasks"], data["next_id"])
    except FileNotFoundError:
        return ([], 1)


def add_task(description):
    """Add a new task with the given description."""
    global next_id  # allows updating global counter

    if not description or not isinstance(description, str):
        print("Error: Task description must be a non empty string. ")
        return
    if len(description) > 200:
        print("Error: Description too long (max 200 characters).")
        return
    new_task = {
        "id": next_id,
        "description": description,
        "completed": False,
    }

    tasks.append(new_task)
    next_id += 1
    save_tasks()  #


def list_all_tasks():
    """lists all the tasks that are completed or in process"""
    for task in tasks:
        status = "done" if task["completed"] else "pending"
        print(f"[{task['id']}] {task['description']} - {status}")


def list_pending_tasks():
    """Filter unfinished tasks"""
    pending = [t for t in tasks if not t["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    for task in pending:
        print(f"[{task['id']}] {task['description']}")


def list_completed_tasks():
    """ Filter finished tasks"""
    completed = [t for t in tasks if t["completed"]]

    if not completed:
        print("No completed tasks.")
        return

    for task in completed:
        print(f"[{task['id']}] {task['description']}")


def get_task_by_id(task_id):
    """Find matching task by ID"""
    matches = [t for t in tasks if t["id"] == task_id]
    return matches[0] if matches else None


def complete_task(task_id):
    """Mark a task as completed by its ID."""
    if not isinstance(task_id, int) or task_id <1:
        print("Error: Task ID must be a positive integer. ")
        return
    task = get_task_by_id(task_id)

    if task:
        task["completed"] = True
        save_tasks()
    else:
        print(f"Task with ID {task_id} not found")


def search_tasks(query):
    """Case-insensitive search in task descriptions"""
    results = [
        t for t in tasks
        if query.lower() in t["description"].lower()
    ]

    if not results:
        print(f"No task matching '{query}'.")
        return

    for task in results:
        status = "done" if task["completed"] else "pending"
        print(f"[{task['id']}] {task['description']} - {status}")


# Load saved data when program starts
tasks, next_id = load_tasks()

def delete_task(task_id):
    """Remove a task by ID. Print error if not found"""
    global tasks
    task = get_task_by_id(task_id)
    if not task:
        print(f"Task with ID {task_id} not found.")
        return
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks()
    print(f"Task {task_id} deleted.")



def main():
    parser = argparse.ArgumentParser(description="A simple task tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    #"add" command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # "list" command
    subparsers.add_parser("list", help="List all tasks")
    
    # "complete" command
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument("id", type=int, help="Task ID")

    #"delete" command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # "search " command
    search_parser = subparsers.add_parser("search", help="Search tasks")
    search_parser.add_argument("query", type=str, help="search query")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
        print(f"Task added: {args.description}")

    elif args.command == "list":
        list_all_tasks()
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "search":
        search_tasks(args.query)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
