import json, os
from ai.trends.trend_tracker import get_trends_for_niche
from ai.events.event_suggester import get_upcoming_events

def generate_captions():
    trends = get_trends_for_niche()
    events = get_upcoming_events()

    captions = []
    for trend in trends:
        for event in events:
            captions.append(f"Don't miss our {event['event']}! Featuring {trend} 🌟")

    return captions
