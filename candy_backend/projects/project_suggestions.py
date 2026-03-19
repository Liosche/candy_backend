from datetime import datetime

def project_suggestions(projects: dict):
    suggestions = []

    for pid, p in projects.items():
        prio = p.get("priority", 0)

        if prio > 0.7:
            suggestions.append(f"{pid} wäre heute sinnvoll weiterzuführen.")

        if p["open_tasks"]:
            suggestions.append(f"Bei {pid} gibt es noch offene Aufgaben.")

        if p["activity"]:
            last = datetime.fromisoformat(p["activity"][-1]["timestamp"])
            days = (datetime.now() - last).days
            if days >= 3:
                suggestions.append(f"{pid} hast du seit {days} Tagen nicht angerührt.")

    return suggestions
