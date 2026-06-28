import random

AUTHOR = "ShivamMishra1603"

PRIMARY_COLORS = ["red", "blue", "yellow"]

MIX_RESULTS = {
    frozenset(["red", "yellow"]): "orange",
    frozenset(["red", "blue"]): "purple",
    frozenset(["blue", "yellow"]): "green",
    frozenset(["red", "red"]): "red",
    frozenset(["blue", "blue"]): "blue",
    frozenset(["yellow", "yellow"]): "yellow",
}

VALID_GUESSES = sorted(set(MIX_RESULTS.values()))


def mix_colors(color_a, color_b):
    return MIX_RESULTS[frozenset([color_a, color_b])]


def run():
    print(f"=== Color Mixer ===")
    print(f"Game by {AUTHOR}\n")
    print("Mix two primary colors (red, blue, yellow) to get a new color!")
    print(f"Possible results: {', '.join(VALID_GUESSES)}")
    print("Type 'q' at any time to quit.\n")

    score = 0
    round_num = 0

    while True:
        round_num += 1
        color_a = random.choice(PRIMARY_COLORS)
        color_b = random.choice(PRIMARY_COLORS)
        correct = mix_colors(color_a, color_b)

        print(f"--- Round {round_num} (Score: {score}) ---")
        print(f"Mix these colors: {color_a} + {color_b}")

        guess = input("What color do you get? ").strip().lower()

        if guess == "q":
            round_num -= 1
            break


        if guess not in VALID_GUESSES:
            print(f"Invalid guess! Choose from: {', '.join(VALID_GUESSES)}")
            round_num -= 1
            continue

        if guess == correct:
            score += 1
            print(f"Correct! {color_a} + {color_b} = {correct} 🎨")
        else:
            print(f"Wrong! {color_a} + {color_b} = {correct}, not {guess}.")

        print(f"Current score: {score}/{round_num}\n")

    print(f"\nThanks for playing! Final score: {score}/{round_num if round_num else 0}")
