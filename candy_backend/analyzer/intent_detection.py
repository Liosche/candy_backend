def detect_intent(text: str):
    t = text.lower()

    if "tag" in t or "heute" in t:
        return "ask_day_plan"

    if "konzentrieren" in t or "fokus" in t:
        return "start_focus"

    if "reflekt" in t or "reflexion" in t:
        return "ask_reflection"

    return "general"
