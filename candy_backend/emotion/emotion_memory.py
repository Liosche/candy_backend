import json
from datetime import datetime
from pathlib import Path

class EmotionMemory:
    def __init__(self, path="memory/emotions.json"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            self.data = json.loads(self.path.read_text())
        else:
            self.data = {"history": []}
            self.save()

    def save(self):
        self.path.write_text(json.dumps(self.data, indent=4))

    def add(self, emotion, intensity):
        self.data["history"].append({
            "emotion": emotion,
            "intensity": intensity,
            "timestamp": datetime.now().isoformat()
        })
        self.save()
