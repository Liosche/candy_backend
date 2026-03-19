from datetime import datetime

class FocusMode:
    def __init__(self, memory):
        self.memory = memory

    def start(self, duration, project_id):
        session = {
            "project": project_id,
            "duration": duration,
            "start": datetime.now().isoformat(),
            "state": "focus"
        }
        self.memory["focus_session"] = session
        return session

    def break_phase(self):
        session = self.memory.get("focus_session")
        if not session:
            return None
        session["state"] = "break"
        session["break_start"] = datetime.now().isoformat()
        return session

    def finish(self, mood):
        session = self.memory.get("focus_session")
        if not session:
            return None

        session["end"] = datetime.now().isoformat()
        session["end_mood"] = mood

        if "focus_sessions" not in self.memory:
            self.memory["focus_sessions"] = []
        self.memory["focus_sessions"].append(session)

        self.memory["focus_session"] = None
        return session
