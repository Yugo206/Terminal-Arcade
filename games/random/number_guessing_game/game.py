import random

AUTHOR = "TheGittyPerson"


def run():
    print(f"Game by {AUTHOR}")

    number = random.randint(1, 100)
    tries = 6
    print(f"\nTry to guess the number in {tries} tries.")
    while tries > 0:
        if not (inp := input("\nEnter a number 1~100: ")).isdigit():
            print("\nInvalid input: Only enter digits. Try again.")
            continue

        inp = int(inp)

        if inp < 1 or inp > 100:
            print("\nInvalid input: Only enter numbers from 1 to 100. Try "
                  "again.")
            continue

        if inp == number:
            print(f"\nCorrect! The number is indeed {number}.")
            return

        if inp < number:
            print("\nToo low! Try again.")
        if inp > number:
            print("\nToo high! Try again.")

        tries -= 1
        print(f"Remaining tries: {tries}")

    print("\nYou ran out of tries :(")
    print(f"The number was {number}.")
