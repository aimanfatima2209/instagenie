from ai.generators.caption_generator import generate_captions
from ai.trends.trend_tracker import get_trends_for_niche
from ai.events.event_suggester import get_events_for_niche

# Test caption generation
captions = generate_captions("travel", "funny", "sunset at Marina Bay", 3, 140, 2)
print("Generated Captions:", captions)

# Test trends for niche
niche = "travel"
print(f"Popular {niche} trends:", get_trends_for_niche(niche))

# Test events for niche
print(f"Upcoming {niche} events:", get_events_for_niche(niche))
