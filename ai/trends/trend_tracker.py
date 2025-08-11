import json
import os

def get_trends_for_niche(niche):
    """
    Returns popular trends filtered by niche
    """
    trends_path = os.path.join("ai", "trends", "trends.json")

    with open(trends_path, "r") as f:
        trends = json.load(f)

    # Filter trends by popularity + niche match
    popular_trends = [
        t["trend"] for t in trends
        if t["popularity"] > 70 and (niche.lower() in t.get("niche", "").lower())
    ]
    return popular_trends
