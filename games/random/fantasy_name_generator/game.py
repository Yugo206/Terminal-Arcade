import random

AUTHOR = "TomGiar"

# Predefined syllables to build names
prefixes = ["Val", "Thal", "Kri", "Mor", "Eld", "Dra", "Zan", "Vor"]
middles  = ["do", "a", "i", "or", "en", "al", "ir", "om"]
suffixes = ["rin", "or", "mor", "in", "eth", "ar", "ix", "on"]

def generate_name():
    """Generates a fantasy name by combining random syllables."""
    parts = [random.choice(prefixes)]
    # With some probability, adds a middle syllable
    if random.random() > 0.5:
        parts.append(random.choice(middles))
    parts.append(random.choice(suffixes))
    return "".join(parts)

def run():
    print("=== Fantasy Name Generator ===\n")
    try:
        count = int(input("How many names do you want to generate? (1-20): "))
        count = max(1, min(count, 20))
    except ValueError:
        count = 5

    print(f"\nHere are your {count} fantasy names:\n")
    for _ in range(count):
        print(f"  * {generate_name()}")
    print()