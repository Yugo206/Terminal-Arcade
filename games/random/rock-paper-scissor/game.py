import random

CHOICES = ["rock", "paper", "scissors"]


def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    
    while choice not in CHOICES:
        print("Invalid choice. Please try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    
    return choice


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "user"
    
    return "computer"


def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    
    if result == "user":
        print("You win!")
    elif result == "computer":
        print("Computer wins!")
    else:
        print("It's a tie!")
    
    return result


def run():
    print("🎮 Rock Paper Scissors")

    user_score = 0
    computer_score = 0

    while True:
        result = play_round()
        
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break

    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")
    
    
