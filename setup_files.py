import os, json

# Define folder structure
folders = [
    "ai",
    "ai/trends",
    "ai/prompts",
    "ai/generators",
    "ai/events",
    "ai/utils"
]

# Create folders and __init__.py for packages
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    init_file = os.path.join(folder, "__init__.py")
    if not os.path.exists(init_file):
        open(init_file, "w").close()

# trends.json
trends_data = [
    {"trend": "AI-powered captions", "popularity": 85},
    {"trend": "Travel photography", "popularity": 72},
    {"trend": "Eco-friendly living tips", "popularity": 64}
]
with open("ai/trends/trends.json", "w") as f:
    json.dump(trends_data, f, indent=2)

# trend_tracker.py
trend_tracker_code = """import json
import os

def track_trends():
    with open(os.path.join("ai", "trends", "trends.json"), "r") as f:
        trends = json.load(f)
    return [t["trend"] for t in trends if t["popularity"] > 70]
"""
with open("ai/trends/trend_tracker.py", "w") as f:
    f.write(trend_tracker_code)

# prompts.json
prompts_data = {
    "caption": "Write an engaging Instagram caption about {topic}",
    "event": "Suggest an Instagram post idea for {event}"
}
with open("ai/prompts/prompts.json", "w") as f:
    json.dump(prompts_data, f, indent=2)

# caption_generator.py
caption_generator_code = """import json
import os

def generate_caption(topic):
    with open(os.path.join("ai", "prompts", "prompts.json"), "r") as f:
        prompts = json.load(f)
    return prompts["caption"].replace("{topic}", topic)
"""
with open("ai/generators/caption_generator.py", "w") as f:
    f.write(caption_generator_code)

# events.json
events_data = [
    {"event": "Diwali", "idea": "Share colorful diya decoration tips"},
    {"event": "World Environment Day", "idea": "Eco-friendly living ideas"}
]
with open("ai/events/events.json", "w") as f:
    json.dump(events_data, f, indent=2)

# event_suggester.py
event_suggester_code = """import json
import os

def suggest_event_post():
    with open(os.path.join("ai", "events", "events.json"), "r") as f:
        events = json.load(f)
    return [e["idea"] for e in events]
"""
with open("ai/events/event_suggester.py", "w") as f:
    f.write(event_suggester_code)

# test_prompt_run.py
test_script_code = """from ai.trends.trend_tracker import track_trends
from ai.generators.caption_generator import generate_caption
from ai.events.event_suggester import suggest_event_post

print("=== Trend Tracking ===")
print(track_trends())

print("\\n=== AI Caption Generation ===")
print(generate_caption("travel photography"))

print("\\n=== Event-Based Suggestions ===")
print(suggest_event_post())
"""
with open("ai/utils/test_prompt_run.py", "w") as f:
    f.write(test_script_code)

print("✅ All files and folders created successfully!")
