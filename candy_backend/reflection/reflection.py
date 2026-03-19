def daily_reflection(log):
    emotions = [e["emotion"] for e in log.get("emotions", [])]
    projects = log.get("projects", {})
