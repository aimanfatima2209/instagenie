import os
import json

# Helper to create folder if not exists
def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Helper to create file with content
def make_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# === 1. Create folder structure ===
folders = [
    "ai/trends",
    "ai/events",
    "ai/prompts",
    "ai/generators",
    "ai/utils"
]

for folder in folders:
    make_folder(folder)

# === 2. trends.json ===
make_file("ai/trends/trends.json", json.dumps([
    {"trend": "AI-powered captions", "popularity": 85},
    {"trend": "Travel photography", "popularity": 72},
    {"trend": "Eco-friendly living tips", "popularity": 64}
], indent=2))

# === 3. trend_tracker.py ===
make_file("ai/trends/trend_tracker.py", """import json, os

def get_trends_for_niche():
    path = os.path.join("ai", "trends", "trends.json")
    with open(path, "r", encoding="utf-8") as f:
        trends = json.load(f)
    return [t["trend"] for t in trends if t["popularity"] > 70]
""")

# === 4. events.json ===
make_file("ai/events/events.json", json.dumps([
    {"event": "Product launch", "date": "2025-09-10"},
    {"event": "Photography contest", "date": "2025-09-15"},
    {"event": "AI conference", "date": "2025-09-20"}
], indent=2))

# === 5. event_suggester.py ===
make_file("ai/events/event_suggester.py", """import json, os

def get_upcoming_events():
    path = os.path.join("ai", "events", "events.json")
    with open(path, "r", encoding="utf-8") as f:
        events = json.load(f)
    return [e for e in events]  # returns all events
""")

# === 6. prompts.json ===
make_file("ai/prompts/prompts.json", json.dumps({
    "caption_prompt": "Write a catchy Instagram caption for: {trend} and {event}"
}, indent=2))

# === 7. caption_generator.py ===
make_file("ai/generators/caption_generator.py", """import json, os
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
""")

# === 8. test_prompt_run.py (trend test) ===
make_file("ai/utils/test_prompt_run.py", """from ai.trends.trend_tracker import get_trends_for_niche

print("Popular trends:", get_trends_for_niche())
""")

# === 9. test_caption_run.py (caption test) ===
make_file("ai/utils/test_caption_run.py", """from ai.generators.caption_generator import generate_captions

print("Generated captions:")
for c in generate_captions():
    print("-", c)
""")

print("✅ All teammate 3 files created successfully!")
