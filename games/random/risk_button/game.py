import random

AUTHOR = "Julito-Dev"

SAFE_MESSAGES = [
    "Safe... for now.",
    "Nothing happened.",
    "You got lucky!",
    "That was close!",
    "The button seems stable.",
    "Still alive!",
    "No explosion this time."
]

EXPLOSION_MESSAGES = [
    "💥 BOOM!",
    "💥 The button exploded!",
    "💥 Well... that didn't go well.",
    "💥 Better luck next time!"
]

JACKPOT_SCORE = 200

def run():
    points = 0
    risk = 0.1
    
    print("---- RISK BUTTON ----")
    print("Press the Button to earn Points")
    print("But beware: it may explode!\n")
    print(f"Reach {JACKPOT_SCORE} points to win.\n")
    
    
    while True:
        print(f"\nPoints: {points}")
        print(f"Explosion Risk: {risk:.0%}")
        
        action = input(
            "Press ENTER to push the button or type S to cash out."
        ).strip().lower()
        
        if action == "s":
            print(f"You cashed out with {points} Points!")
            return

        if random.random() < risk:
            print(f"\n{random.choice(EXPLOSION_MESSAGES)}")
            print(f"Final Score: {points}")
            print("Game Over")
            return
        
        earned = random.randint(5, 20)
        points += earned
        
        print(f"\n+{earned} points!")
        print(random.choice(SAFE_MESSAGES))

        if points >= JACKPOT_SCORE:
            print("\n🏆 JACKPOT!")
            print("You survived long enough to win!")
            print(f"Final Score: {points}")
            return

        risk += 0.05