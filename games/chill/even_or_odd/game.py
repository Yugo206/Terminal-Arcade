import random

AUTHOR = "ChillGats" # that's me :)

def run():
    print("=== Even or Odd ===")
    print(f"Welcome to Even or Odd by {AUTHOR}!\n")
    
    # Get user input, strip extra spaces, and make it lowercase
    user_choice = input("Guess if the random number is Even or Odd : ").strip().lower()
    
    # Check if the input is valid
    if user_choice not in ["even", "odd"]:
        print("Invalid choice! Please type 'Even' or 'Odd'.")
        return
        
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100) # ! change it if you want a different range
    
    # Determine if the number is even or odd
    # The modulo operator (%) checks the remainder when divided by 2
    if random_number % 2 == 0:
        correct_answer = "even"
    else:
        correct_answer = "odd"
        
    print(f"\nThe random number is {random_number}... meaning it is {correct_answer.capitalize()}!")
    
    # Check if the user guessed correctly
    if user_choice == correct_answer:
        print("🎉 You win!")
    else:
        print("😢 You lose!")

print("=== END ====")
