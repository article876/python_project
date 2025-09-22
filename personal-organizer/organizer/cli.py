from .storage import load_tasks, save_tasks
from .tasks import Task

def next_id(tasks):
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTasks:")
    for t in tasks:
        status = "✓" if t.done else " "
        print(f"[{status}] {t.id}: {t.title} (created: {t.created_at})")
    print()

def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Empty title; aborted.")
        return
    notes = input("Notes (optional): ").strip()
    tid = next_id(tasks)
    task = Task(id=tid, title=title, notes=notes or None)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task #{tid} added.")

def complete_task(tasks):
    try:
        tid = int(input("Enter task id to mark complete: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    for t in tasks:
        if t.id == tid:
            if t.done:
                print("Already completed.")
            else:
                t.done = True
                save_tasks(tasks)
                print(f"Task #{tid} marked complete.")
            return
    print("Task id not found.")

def run():
    tasks = load_tasks()
    while True:
        print("\nPersonal Organizer — options:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            tasks = load_tasks()  # refresh
        elif choice == "3":
            complete_task(tasks)
            tasks = load_tasks()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")