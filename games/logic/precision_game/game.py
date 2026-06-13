import time

AUTHOR = "koteshyelamati"

def run():
    print("Game by", AUTHOR)
    print("\n🎯 PRECISION GAME 🎯")
    print("A counter will start incrementing. Press ENTER to stop it as close to 100 as possible!")
    print("The closer to 100, the better your score.\n")

    input("Press ENTER to start the counter...")

    start = time.time()
    speed = 0.5  # seconds per increment (counter moves at 2 per second)

    print("Counter is running... press ENTER to stop!")
    input()

    elapsed = time.time() - start
    counter = elapsed / speed

    # Score is how close to 100 (max 100)
    distance = abs(counter - 100)
    if distance == 0:
        score = 100
    elif distance >= 100:
        score = 0
    else:
        score = max(0, round(100 - distance))

    print(f"\n🛑 You stopped at: {counter:.1f}")
    print(f"Target was: 100")
    print(f"Distance from 100: {distance:.1f}")

    if distance < 1:
        print("🏆 PERFECT! Incredible precision!")
    elif distance < 5:
        print("🥇 Excellent precision!")
    elif distance < 10:
        print("🥈 Good precision!")
    elif distance < 20:
        print("🥉 Not bad, keep practising!")
    else:
        print("💪 Keep trying — aim for 100!")

    print(f"\n🏁 Final score: {score}/100")
