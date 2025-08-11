# ai/generators/caption_generator.py
def generate_captions(niche, tone="aesthetic", topic="", count=3):
    # For now: return mock results
    captions = [f"{tone.capitalize()} caption {i+1} about {topic or niche}" for i in range(count)]
    hashtags = {"high": ["#viral","#trending"], "medium": ["#socialmedia"], "niche":[f"#{niche}"]}
    return {"captions": captions, "hashtags": hashtags, "reason": "mock"}
