import time
import random

AUTHOR = "ChillGats"

def run():
    print(f"=== ⚡ Reaction Time Test by {AUTHOR} ⚡ ===")
    print("When you see 'GO!', hit the ENTER key as fast as you can.")
    print("Type 'quit' at any time to exit.\n")

    reaction_times = []

    while True:
        ready = input("Press ENTER to start a round (or type 'quit'): ").strip().lower()
        if ready in ['quit', 'q', 'exit']:
            break

        print("\nWait for it...")
        
        wait_time = random.uniform(2.0, 5.0)
        time.sleep(wait_time)

        print("🚨 GO! PRESS ENTER! 🚨")
        
        start_time = time.time()
        input()
        end_time = time.time()
        
        reaction_time = end_time - start_time
        
        # --- THE ANTI-CHEAT FIX ---
        if reaction_time < 0.1:
            print(f"⏱️ Time: {reaction_time:.3f} seconds")
            print("❌ FALSE START! You pressed ENTER before or exactly when the signal appeared.")
            print("That round doesn't count towards your average!")
            print("-" * 30)
            continue # This skips the rest of the loop so the score isn't saved!
        
        # If they didn't cheat, the game continues normally
        reaction_times.append(reaction_time)
        average_time = sum(reaction_times) / len(reaction_times)
        
        print(f"⏱️ Your reaction time: {reaction_time:.3f} seconds!")
        print(f"📊 Average so far:     {average_time:.3f} seconds!\n")
        
        if reaction_time < 0.2:
            print("Rating: superhuman! 👽")
        elif reaction_time < 0.25:
            print("Rating: Pro level! 🎮")
        elif reaction_time < 0.35:
            print("Rating: Fast! 🏃 I recognize a gamer!")
        elif reaction_time < 0.5:
            print("Rating: Average! 🙂")
        else:
            print("Rating: Too slow! 🐢")
        print("-" * 30)

    print("\n" + "=" * 30)
    print("🎮 SESSION STATS 🎮")
    print("=" * 30)
    
    if len(reaction_times) > 0:
        final_average = sum(reaction_times) / len(reaction_times)
        best_time = min(reaction_times)
        print(f"Rounds played: {len(reaction_times)}")
        print(f"Final Average: {final_average:.3f} seconds")
        print(f"Best Time:     {best_time:.3f} seconds 🔥")
    else:
        print("You didn't play any valid rounds!")
        
    print("\nThanks for playing the Reaction Time Test!")
