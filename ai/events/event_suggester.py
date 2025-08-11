# ai/events/event_suggester.py
import json
import os

def suggest_events(niche):
    """Return upcoming events relevant to the niche from JSON."""
    file_path = os.path.join("ai", "events", "events.json")
    with open(file_path, "r") as f:
        events = json.load(f)

    return [event for event in events if niche.lower() in event["niche"].lower()] or events
