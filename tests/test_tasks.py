import tempfile
from organizer.tasks import Task
from organizer.storage import save_tasks, load_tasks
from pathlib import Path

def test_task_save_and_load(tmp_path):
    fn = tmp_path / "data.json"
    from organizer import storage
    storage.DATA_FILE = fn

    tasks = [Task(id=1, title="Test", done=False)]
    save_tasks(tasks)
    assert fn.exists()
    loaded = load_tasks()
    assert len(loaded) == 1
    assert loaded[0].title == "Test"