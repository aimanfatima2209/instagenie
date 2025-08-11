import json
import os
from openai import OpenAI

client = OpenAI()

# Load prompts from JSON
def load_prompts():
    path = os.path.join("ai", "prompts", "prompts.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

PROMPTS = load_prompts()

def generate_captions(niche, tone, topic):
    prompt_template = PROMPTS["caption_generation"].get(niche, {}).get(tone)
    if not prompt_template:
        raise ValueError(f"No prompt found for niche '{niche}' and tone '{tone}'")
    
    prompt = prompt_template.format(topic=topic)
    
    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )
    
    return response.output_text

def generate_hashtags(niche):
    prompt_template = PROMPTS["hashtags_generation"]["default"]
    prompt = prompt_template.format(niche=niche)

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text

def generate_event_ideas(event_name, niche):
    prompt_template = PROMPTS["event_based"]["default"]
    prompt = prompt_template.format(event_name=event_name, niche=niche)

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text
