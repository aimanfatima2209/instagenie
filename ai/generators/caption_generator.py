import json
import os
import random

def load_prompts():
    with open(os.path.join("ai", "prompts", "prompts.json"), "r") as f:
        return json.load(f)

def generate_caption(niche, tone, topic="sunset at Marina Bay", count=3, max_chars=140, emoji_count=2):
    prompts = load_prompts()
    prompt_data = next((p for p in prompts if p["niche"] == niche), None)
    if not prompt_data:
        return {"error": f"No prompts found for niche '{niche}'"}

    # For now — mock captions instead of calling OpenAI API
    captions = [f"{tone.title()} caption {i+1} about {topic} 🌅" for i in range(count)]
    hashtags = {
        "high": ["#viral", "#trending"],
        "medium": ["#socialmedia", "#creativity"],
        "niche": [f"#{niche}"]
    }
    return {"captions": captions, "hashtags": hashtags, "reason": "Mock data for testing"}
