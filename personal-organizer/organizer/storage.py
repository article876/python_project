import json
from typing import List
from .tasks import Task
from pathlib import Path

DATA_FILE = Path("data.json")

def load_tasks() -> List[Task]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    tasks = [Task(**item) for item in data]
    return tasks

def save_tasks(tasks: List[Task]):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2, ensure_ascii=False)