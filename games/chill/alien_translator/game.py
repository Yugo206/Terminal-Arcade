import random

AUTHOR = "Shivank Sharma"

ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def build_static_mapping(seed=None):
    """Build a deterministic letter->letter substitution map.

    Each letter of the alphabet maps to a single alien letter. Reusing the
    same seed produces the same mapping (useful for translating back and
    forth with a friend). A random seed gives a fresh cipher each session.
    """
    rng = random.Random(seed)
    shuffled = ALPHABETS.copy()
    rng.shuffle(shuffled)
    return {a: b for a, b in zip(ALPHABETS, shuffled)}

def translate(message, mapping, mode):
    """Translate a message using the chosen mode.

    mode == "static"     -> look up each letter in the mapping dict.
    mode == "randomized" -> pick a random letter for each alphabet char.
    """
    out = []
    for char in message:
        upper = char.upper()
        if upper in ALPHABETS:
            if mode == "static":
                replacement = mapping[upper]
            else:
                replacement = random.choice(ALPHABETS)
            # Preserve original case so 'Hello' stays 'AbcDe' shape, not 'ABCDE'.
            out.append(replacement.lower() if char.islower() else replacement)
        else:
            out.append(char)
    return ''.join(out)

def choose_mode():
    """Prompt the user until they pick a valid mode."""
    print("Choose a cipher mode:")
    print("  1) static     - each letter maps to the same alien letter every time")
    print("  2) randomized - each letter is replaced with a random letter")
    while True:
        choice = input("Enter 1 or 2 (or 'quit' to exit): ").strip().lower()
        if choice in ('quit', 'q', 'exit'):
            return None
        if choice in ('1', 'static', 's'):
            return "static"
        if choice in ('2', 'randomized', 'random', 'r'):
            return "randomized"
        print("Invalid choice. Please enter 1 (static) or 2 (randomized).")

def run():
    print('Translate your message to alien language!')
    mode = choose_mode()
    if mode is None:
        print("Exiting Alien Translator. Goodbye!")
        return

    if mode == "static":
        # Build the cipher once so every message in this session is consistent.
        mapping = build_static_mapping()
        reverse_mapping = {v: k for k, v in mapping.items()}
        print("Static cipher ready. Type 'decode' to switch to decode mode, 'quit' to exit.")
        decoding = False
    else:
        mapping = None
        reverse_mapping = None
        decoding = False

    while True:
        prompt = "Enter your message"
        if mode == "static":
            prompt += " (or 'decode' to translate back, 'quit' to exit)"
        else:
            prompt += " (or type 'quit' to exit)"
        message = input(prompt + ": ")

        lower = message.lower()
        if lower in ('quit', 'q', 'exit'):
            print("Exiting Alien Translator. Goodbye!")
            break
        if mode == "static" and lower in ('decode', 'd'):
            decoding = not decoding
            state = "ON" if decoding else "OFF"
            print(f"Decode mode is now {state}.")
            continue

        if decoding and reverse_mapping is not None:
            translated_message = []
            for char in message:
                upper = char.upper()
                if upper in reverse_mapping:
                    replacement = reverse_mapping[upper]
                    translated_message.append(replacement.lower() if char.islower() else replacement)
                else:
                    translated_message.append(char)
            print("Decoded message: " + ''.join(translated_message) + "\n")
        else:
            result = translate(message, mapping, mode)
            label = "Translated" if not decoding else "Decoded"
            print(f"{label} to Alien Language: {result}\n")
