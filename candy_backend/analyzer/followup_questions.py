def followup_question(reason: str, projects: list):
    if reason == "unclear_project":
        names = ", ".join([p["name"] for p in projects])
        return f"Meinst du eines deiner Projekte? {names}?"
    return None
