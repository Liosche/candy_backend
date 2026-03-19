from emotion.emotion import detect_emotion
from emotion.emotion_score import emotion_intensity
from emotion.emotion_memory import EmotionMemory

from memory.context_memory import ContextMemory
from memory.project_memory import ProjectMemory

from ssml.ssml_selector import select_ssml_preset
from ssml.ssml_builder import build_ssml

from analyzer.intent_detection import detect_intent
from analyzer.ambiguity import detect_ambiguity
from analyzer.followup_questions import followup_question
from analyzer.confirmation import confirmation_needed, confirmation_prompt
from analyzer.summary import summarize_project

from projects.project_activity import detect_project_activity
from projects.project_priority import compute_priority
from projects.project_patterns import analyze_patterns
from projects.project_suggestions import project_suggestions

from dayplanner.day_planner import build_day_plan
from focus.focus_mode import FocusMode
from reflection.reflection import daily_reflection

emotion_mem = EmotionMemory()
context_mem = ContextMemory()
project_mem = ProjectMemory()
focus = FocusMode(context_mem.data)

def analyze(text: str):
    emotion = detect_emotion(text)
    intensity = emotion_intensity(text)
    emotion_mem.add(emotion, intensity)

    intent = detect_intent(text)

    amb = detect_ambiguity(text, project_mem.get_all())
    if amb:
        return {
            "message": followup_question(amb, project_mem.get_all()),
            "action": "ask_clarification"
        }

    pid = detect_project_activity(text, project_mem.get_all())
    if pid:
        project_mem.add_activity(pid, emotion)
        p = project_mem.get(pid)
        p["priority"] = compute_priority(p)
        patterns = analyze_patterns(p)
        suggestions = project_suggestions(project_mem.data["projects"])

        return {
            "message": f"Ich sehe, du arbeitest an {pid}.",
            "patterns": patterns,
            "suggestions": suggestions,
            "action": "project_detected",
            "meta": {"project_id": pid}
        }

    if intent == "ask_day_plan":
        plan = build_day_plan(emotion, intensity, project_mem.data["projects"])
        return {
            "message": "Ich habe deinen Tag strukturiert.",
            "plan": plan,
            "action": "show_plan"
        }

    if intent == "start_focus":
        last = project_mem.get_last_focus()
        return {
            "message": "Wie lange möchtest du fokussiert arbeiten? 25 oder 45 Minuten?",
            "action": "ask_focus_duration",
            "meta": {"project_id": last["id"] if last else None}
        }

    if intent == "ask_reflection":
        ref = daily_reflection(context_mem.data)
        return {
            "message": ref["summary"],
            "question": ref["question"],
            "action": "ask_reflection"
        }

    preset = select_ssml_preset(emotion, intensity)
    ssml = build_ssml(text, preset)

    return {
        "message": "Okay. Erzähl mir mehr.",
        "emotion": emotion,
        "intensity": intensity,
        "ssml": ssml,
        "action": None
    }
