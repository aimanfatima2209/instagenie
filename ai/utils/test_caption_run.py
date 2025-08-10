from ai.generators.caption_generator import generate_captions

print("Generated captions:")
for c in generate_captions():
    print("-", c)
