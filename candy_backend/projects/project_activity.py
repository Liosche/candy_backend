def detect_project_activity(text: str, projects: list):
    t = text.lower()
    for p in projects:
        if p["name"].lower() in t:
            return p["id"]
    return None
