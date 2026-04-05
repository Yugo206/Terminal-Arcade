import random

def coin_flip():
    print("Welcome to Coin Flip!")

    user_choice = input("Guess heads or tails: ").lower()

    if user_choice not in ["heads", "tails"]:
        print("Invalid choice! Please choose heads or tails.")
        return

    result = random.choice(["heads", "tails"])
    print(f"Coin landed on: {result}")

    if user_choice == result:
        print("🎉 You win!")
    else:
        print("😢 You lose!")

if __name__ == "__main__":
    coin_flip()
