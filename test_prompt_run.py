from ai.trends.trend_tracker import track_trends
from ai.generators.caption_generator import generate_caption
from ai.events.event_suggester import suggest_event_post

print("=== Trend Tracking ===")
print(track_trends())

print("=== AI Caption Generation ===")
print(generate_caption("travel photography"))

print("=== Event-Based Suggestions ===")
print(suggest_event_post())
