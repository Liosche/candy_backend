def detect_ambiguity(text: str, projects: list):
    t = text.lower()

    if "weiter" in t and len(projects) > 1:
        return "unclear_project"

    return None
