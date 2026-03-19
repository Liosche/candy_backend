def confirmation_needed(intent: str):
    return intent in ["continue_project"]

def confirmation_prompt(intent: str, project_name: str):
    return f"Willst du wirklich bei {project_name} weitermachen?"
