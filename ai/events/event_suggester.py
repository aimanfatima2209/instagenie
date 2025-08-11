import json
import os
from datetime import datetime

def get_events_for_niche(niche):
    """
    Returns upcoming events relevant to a niche
    """
    events_path = os.path.join("ai", "events", "events.json")

    with open(events_path, "r") as f:
        events = json.load(f)

    today = datetime.today().strftime("%Y-%m-%d")

    relevant_events = [
        e for e in events
        if niche.lower() in e.get("niche", "").lower() and e["date"] >= today
    ]
    return relevant_events
