from services.openai_service import generate_captions_and_hashtags
from ai.trends.trend_tracker import get_trends_for_niche
from ai.events.event_suggester import suggest_events

print("🚀 InstaGenie – Teammate 3 AI Module Test\n")

niche = "travel"

print(f"📌 Generated Captions & Hashtags for niche: {niche}")
captions_output = generate_captions_and_hashtags(
    niche, tone="funny", topic="sunset at Marina Bay 🌅", count=3, use_mock=True
)
print(captions_output, "\n")

print(f"🔥 Popular Trends in niche: {niche}")
trends_output = get_trends_for_niche(niche, use_mock=True)
print(trends_output, "\n")

print(f"🎯 Upcoming Events for niche: {niche}")
events_output = suggest_events(niche, use_mock=True)
print(events_output, "\n")

print("✅ All Teammate 3 modules are working and returning mock/test data successfully!")
