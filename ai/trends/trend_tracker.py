# ai/trends/trend_tracker.py
import json
import os

def get_trends_for_niche(niche):
    """Filter trends by popularity > 70 and optionally niche keyword."""
    file_path = os.path.join("ai", "trends", "trends.json")
    with open(file_path, "r") as f:
        trends = json.load(f)

    popular_trends = [t["trend"] for t in trends if t["popularity"] > 70]

    # Optional: niche keyword filtering
    return [trend for trend in popular_trends if niche.lower() in trend.lower()] or popular_trends
