import json, os

def get_upcoming_events():
    path = os.path.join("ai", "events", "events.json")
    with open(path, "r", encoding="utf-8") as f:
        events = json.load(f)
    return [e for e in events]  # returns all events
