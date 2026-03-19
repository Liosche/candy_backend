def summarize_project(project: dict):
    tasks = project["open_tasks"]
    mood = project["last_mood"]

    summary = []

    if tasks:
        summary.append(f"Offene Aufgaben: {len(tasks)}")

    if mood:
        summary.append(f"Letzte Stimmung: {mood}")

    return " • ".join(summary)
