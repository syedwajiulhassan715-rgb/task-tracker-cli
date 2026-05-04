
tasks = []
next_id = 1

def add_task(description):
    global next_id
    new_task = {
        "id": next_id,
        "description": description,
        "completed": False,
    }
    tasks.append(new_task)
    next_id += 1

def list_all_tasks():
    for task in tasks:
        status = "done" if task["completed"] else "pending"
        print(f"[{task['id']}] {task['description']} - {status}")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return
    print(f"Task with ID {task_id} not found")

add_task("Learn Python")
add_task("Build task tracker")
add_task("Apply to internships")
list_all_tasks()
complete_task(2)
list_all_tasks()
complete_task(99)

