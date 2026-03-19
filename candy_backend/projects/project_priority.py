from datetime import datetime

def compute_priority(project: dict):
    score = 0.0

    score += project["priority"] * 0.4
    score += min(len(project["open_tasks"]) * 0.1, 0.3)

    mood = project.get("last_mood")
    if mood == "positive":
        score += 0.2
    if mood == "stressed":
        score -= 0.1

    if project["activity"]:
        last = datetime.fromisoformat(project["activity"][-1]["timestamp"])
        days = (datetime.now() - last).days
        score += min(days * 0.05, 0.3)

    return max(0.0, min(1.0, score))
