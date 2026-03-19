from datetime import datetime

def estimate_energy(emotion: str, intensity: float):
    base = 0.6

    if emotion == "tired":
        base -= 0.3 * intensity
    if emotion == "stressed":
        base -= 0.15 * intensity
    if emotion == "positive":
        base += 0.2 * intensity

    hour = datetime.now().hour
    if hour < 10:
        base += 0.1
    if hour > 20:
        base -= 0.2

    return max(0.1, min(1.0, base))


def pick_top_projects(projects: dict, limit=2):
    scored = []
    for pid, p in projects.items():
        prio = p.get("priority", 0.5)
        scored.append((pid, prio))
    scored.sort(key=lambda x: x[1], reverse=True)
    return [pid for pid, _ in scored[:limit]]


def build_day_plan(emotion: str, intensity: float, projects: dict):
    energy = estimate_energy(emotion, intensity)
    top = pick_top_projects(projects)

    plan = []

    plan.append({
        "type": "focus",
        "project": top[0] if top else None,
        "duration": 45 if energy > 0.6 else 25
    })

    plan.append({
        "type": "light",
        "project": top[1] if len(top) > 1 else top[0],
        "duration": 20
    })

    if energy > 0.5:
        plan.append({
            "type": "focus",
            "project": top[0],
            "duration": 30
        })

    plan.append({
        "type": "break",
        "duration": 10
    })

    return plan
