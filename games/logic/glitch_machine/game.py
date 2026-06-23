"""
Glitch Machine
A corrupted word flashes on screen, replacing some of its letters with
random symbols (e.g. TERMINAL -> T#RM!N@L). The player must type the
original, uncorrupted word before the glitch overtakes the system.

Play multiple rounds and rack up points - score increases with word
length and decreases the longer you take to answer.
"""

import random
import string
import time

WORDS = [
    "TERMINAL", "PYTHON", "KEYBOARD", "COMPILER", "FUNCTION",
    "VARIABLE", "ALGORITHM", "DEBUGGER", "ARCADE", "GLITCH",
    "PROGRAM", "CONSOLE", "SCRIPT", "BINARY", "NETWORK",
    "PROCESS", "MACHINE", "SIGNAL", "MEMORY", "MODULE",
]

GLITCH_SYMBOLS = "#!@$%&*?^~"

ROUNDS_PER_GAME = 5


def corrupt_word(word, difficulty=0.4):
    """Replace a portion of the word's letters with random glitch symbols.

    At least one letter is always corrupted so the puzzle is never trivial,
    and at least one letter is always left visible as a hint.
    """
    word_chars = list(word)
    length = len(word_chars)

    num_to_corrupt = max(1, round(length * difficulty))
    num_to_corrupt = min(num_to_corrupt, length - 1) if length > 1 else 0

    indices = list(range(length))
    random.shuffle(indices)
    corrupt_indices = set(indices[:num_to_corrupt])

    corrupted_chars = [
        random.choice(GLITCH_SYMBOLS) if i in corrupt_indices else ch
        for i, ch in enumerate(word_chars)
    ]
    return "".join(corrupted_chars)


def print_banner():
    print("=" * 40)
    print("        G L I T C H   M A C H I N E")
    print("=" * 40)
    print("A corrupted string flickers across the terminal.")
    print("Type the original word before the system glitches out!")
    print("-" * 40)


def play_round(round_num, used_words):
    available = [w for w in WORDS if w not in used_words]
    if not available:
        available = WORDS
        used_words.clear()

    word = random.choice(available)
    used_words.add(word)

    corrupted = corrupt_word(word)

    print(f"\nRound {round_num}/{ROUNDS_PER_GAME}")
    print(f"Corrupted signal: {corrupted}")

    start_time = time.time()
    guess = input("Decode it > ").strip().upper()
    elapsed = time.time() - start_time

    if guess == word:
        base_points = len(word) * 10
        time_penalty = int(elapsed) * 2
        points = max(5, base_points - time_penalty)
        print(f"Signal restored! It was {word}. (+{points} points)")
        return points
    else:
        print(f"Decryption failed. The word was {word}.")
        return 0


def run():
    print_banner()

    score = 0
    used_words = set()

    for round_num in range(1, ROUNDS_PER_GAME + 1):
        score += play_round(round_num, used_words)
        print(f"Current score: {score}")

    print("\n" + "=" * 40)
    print(f"GAME OVER - Final Score: {score}")
    if score >= 200:
        print("Signal integrity: EXCELLENT")
    elif score >= 100:
        print("Signal integrity: STABLE")
    else:
        print("Signal integrity: CRITICAL")
    print("=" * 40)

