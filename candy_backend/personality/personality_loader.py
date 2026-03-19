import json
from pathlib import Path

class Personality:
    def __init__(self, path="personality/personality.json"):
        self.path = Path(path)
        self.data = json.loads(self.path.read_text())

    def apply(self, response: str, emotion: str):
        core = self.data["core_personality"]
        mods = self.data["situational_modifiers"].get(emotion, {})

        tone = mods.get("tone", core["tone"])
        warmth = core["warmth"] + mods.get("warmth", 0)
        directness = core["directness"] + mods.get("directness", 0)
        humor = core["humor"] + mods.get("humor", 0)

        # Tonalität anwenden
        if tone == "whisper":
            response = f"(leise) {response}"

        # Wärme
        if warmth > 0.8:
            response = f"{response} Ich bin bei dir."

        # Direktheit
        if directness < 0.4:
            response = f"Vielleicht… {response}"

        # Humor
        if humor > 0.3:
            response += " (kleines Lächeln)"

        return response
