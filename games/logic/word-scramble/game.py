import random

AUTHOR = "lagback"


WORDS = [
    "python",
    "script",
    "terminal",
    "program",
    "variable",
    "function",
    "computer",
    "keyboard",
    "monitor",
    "internet",
    "database",
    "network",
    "binary",
    "system",
    "memory",
]


def scramble_word(word):
    letters = list(word)
    while "".join(letters) == word:
        random.shuffle(letters)
    return "".join(letters)


def run():
    print(f"Game by {AUTHOR}")
    print("=== Word Scramble ===")

    score = 0
    rounds = 3

    for i in range(rounds):
        word = random.choice(WORDS)
        scrambled = scramble_word(word)

        print(f"\nRound {i + 1}/{rounds}")
        print(f"Scrambled word: {scrambled}\n")

        try:
            guess = input("Your answer: ").strip().lower()
        except EOFError:
            break

        if guess == word:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The word was: {word}\n")

    print(f"\n=== Final Score: {score}/{rounds} ===")
    if score == rounds:
        print("Perfect! Word master!")
    elif score >= rounds // 2:
        print("Not bad! Keep practicing.")
    else:
        print("Better luck next time!")
