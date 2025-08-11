def generate_captions(topic, tone, count=3, max_chars=140, emoji_count=2, niche=None):
    """
    Mock caption generator with optional niche parameter.
    Replace later with OpenAI API logic from backend.
    """
    captions = [f"{tone.capitalize()} caption {i+1} about {topic}" for i in range(count)]
    hashtags = {
        "high": ["#viral", "#trending"],
        "medium": ["#socialmedia", "#creativity"],
        "niche": [f"#{niche}"] if niche else []
    }
    return {
        "captions": captions,
        "hashtags": hashtags,
        "reason": "Mock data for testing"
    }
