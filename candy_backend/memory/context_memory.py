import json
from pathlib import Path

class ContextMemory:
    def __init__(self, path="memory/context.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {"projects": {}, "emotions": [], "focus_sessions": []}
            self.save()

    def save(self):
        self.path.write_text(json.dumps(self.data, indent=4))
