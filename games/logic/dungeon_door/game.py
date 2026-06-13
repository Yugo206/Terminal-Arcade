import random

AUTHOR = "maitriupadhyay03-cell"

def run():
    print(f"Game by {AUTHOR}")
    print()
    print("=== Dungeon Door ===")
    print()
    print("You stand before three doors.")
    print("One hides a treasure. The others... not so much.")
    print()

    winning_door = random.randint(1, 3)
    attempts = 3
    found = False

    while attempts > 0:
        try:
            choice = int(input(f"Pick a door (1, 2, or 3) -- {attempts} attempt(s) left: "))
        except ValueError:
            print("Enter a number between 1 and 3.")
            continue

        if choice < 1 or choice > 3:
            print("That's not a valid door.")
            continue

        attempts -= 1

        if choice == winning_door:
            print()
            print("You swing the door open and find a chest full of gold!")
            print("You win!")
            found = True
            break
        else:
            if attempts > 0:
                print("Nothing but darkness behind that door. Try again.")
            else:
                print("Wrong again. The dungeon swallows you whole.")

    if not found:
        print()
        print(f"The treasure was behind door {winning_door}. Better luck next time.")
