def emotion_intensity(text: str):
    strong = ["sehr", "extrem", "total"]
    weak = ["etwas", "ein bisschen"]

    score = 0.5
    t = text.lower()

    if any(w in t for w in strong):
        score += 0.3
    if any(w in t for w in weak):
        score -= 0.2

    return max(0.0, min(1.0, score))
