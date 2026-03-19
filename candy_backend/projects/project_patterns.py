from datetime import datetime

def analyze_patterns(project: dict):
    activity = project["activity"]
    if not activity:
        return []

    patterns = []

    hours = [datetime.fromisoformat(a["timestamp"]).hour for a in activity]
    avg_hour = sum(hours) / len(hours)

    if avg_hour < 12:
        patterns.append("Du arbeitest meistens morgens daran.")
    else:
        patterns.append("Du arbeitest oft später am Tag daran.")

    moods = [a["mood"] for a in activity]
    if moods.count("stressed") > len(moods) * 0.4:
        patterns.append("Du wirkst dabei oft gestresst.")

    return patterns
