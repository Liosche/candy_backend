from fastapi import FastAPI
from analyzer.analyze_text import analyze

app = FastAPI()

@app.post("/analyze")
async def analyze_endpoint(payload: dict):
    text = payload.get("text", "")
    result = analyze(text)
    return result
