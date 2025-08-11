from ai.generators.caption_generator import generate_caption
from ai.trends.trend_tracker import get_trends_for_niche

# Choose a test niche and tone
niche = "travel"
tone = "funny"

# Generate captions for testing
print("Generated Captions:", generate_caption(niche, tone))

# Fetch trends for the same niche
print("Popular trends:", get_trends_for_niche(niche))
