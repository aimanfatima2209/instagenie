from ai.generators.caption_generator import generate_captions
from ai.trends.trend_tracker import get_trends_for_niche
from ai.events.event_suggester import suggest_events

# ANSI colors for better terminal output
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

niche = "travel"

print(f"{BOLD}{CYAN}🚀 InstaGenie – Teammate 3 AI Module Test{RESET}\n")

# 1. Generate captions
print(f"{BOLD}{YELLOW}📌 Generated Captions & Hashtags for niche: {niche}{RESET}")
captions_output = generate_captions(niche=niche, tone="funny", topic="sunset at Marina Bay 🌅")
print(f"{GREEN}{captions_output}{RESET}\n")

# 2. Get trends
print(f"{BOLD}{YELLOW}🔥 Popular Trends in niche: {niche}{RESET}")
trends_output = get_trends_for_niche(niche)
print(f"{GREEN}{trends_output}{RESET}\n")

# 3. Suggest events
print(f"{BOLD}{YELLOW}🎯 Upcoming Events for niche: {niche}{RESET}")
events_output = suggest_events(niche)
print(f"{GREEN}{events_output}{RESET}\n")

print(f"{CYAN}✅ All Teammate 3 modules are working and returning mock/test data successfully!{RESET}")
