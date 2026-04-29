
tasks = []
def add_task(description):
    tasks.append(description)
    print(f"Added task: {description}")

add_task("Learn Python")
add_task("Build my first project")
print(tasks)