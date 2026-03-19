import json
from pathlib import Path
from datetime import datetime

class ProjectMemory:
    def __init__(self, path="memory/projects.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {"projects": {}}
            self.save()

    def save(self):
        self.path.write_text(json.dumps(self.data, indent=4))

    def ensure(self, pid):
        if pid not in self.data["projects"]:
            self.data["projects"][pid] = {
                "activity": [],
                "priority": 0.5,
                "open_tasks": [],
                "last_mood": None
            }
            self.save()

    def add_activity(self, pid, mood):
        self.ensure(pid)
        self.data["projects"][pid]["activity"].append({
            "timestamp": datetime.now().isoformat(),
            "mood": mood
        })
        self.save()

    def get(self, pid):
        return self.data["projects"].get(pid)

    def get_all(self):
        return [{"id": pid, "name": pid} for pid in self.data["projects"]]

    def get_last_focus(self):
        if not self.data["projects"]:
            return None
        return list(self.data["projects"].values())[0]
