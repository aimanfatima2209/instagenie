from ai.generators.caption_generator import generate_captions
from ai.trends.trend_tracker import get_trends_for_niche
from ai.events.event_suggester import suggest_events

niche = "travel"

# Captions
captions_data = generate_captions("sunset at Marina Bay", "funny", count=3)
print("\n📝 Generated Captions:")
for cap in captions_data["captions"]:
    print(f"  - {cap}")

# Hashtags
print("\n#️⃣ Hashtags:")
for level, tags in captions_data["hashtags"].items():
    print(f"  {level.capitalize()}: {', '.join(tags)}")

# Trends
trends = get_trends_for_niche(niche)
print(f"\n📈 Popular {niche.capitalize()} Trends:")
for t in trends:
    print(f"  - {t}")

# Events
events = suggest_events(niche)
print(f"\n📅 Upcoming {niche.capitalize()} Events:")
for e in events:
    print(f"  - {e['name']} ({e['date']})")
