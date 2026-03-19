KEYWORDS = {
    "tired": ["müde", "erschöpft", "kaputt"],
    "stressed": ["stress", "überfordert"],
    "sad": ["traurig", "down"],
    "positive": ["gut", "super", "nice"],
    "focused": ["fokus", "konzentriert"]
}

def detect_emotion(text: str):
    t = text.lower()
    for emo, words in KEYWORDS.items():
        if any(w in t for w in words):
            return emo
    return "neutral"
