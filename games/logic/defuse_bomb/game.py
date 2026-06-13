import random
import threading
import time

AUTHOR = "koteshyelamati"

def run():
    print("Game by", AUTHOR)
    print("\n💣 DEFUSE THE BOMB 💣")
    print("A random code has been generated. Enter it before time runs out!\n")

    code_length = 6
    secret_code = "".join([str(random.randint(0, 9)) for _ in range(code_length)])
    time_limit = 15

    print(f"CODE: {secret_code}")
    print(f"You have {time_limit} seconds. Memorise it, then press Enter...")
    input()

    # Clear the code display by printing blank lines
    print("\n" * 3)
    print(f"⏰ Time is ticking! You have {time_limit} seconds to type the code.")
    print("Enter the code: ", end="", flush=True)

    result = {"answer": None}

    def get_input():
        result["answer"] = input()

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()

    start = time.time()
    thread.join(timeout=time_limit)
    elapsed = time.time() - start

    if result["answer"] is None:
        print("\n\n💥 BOOM! Time ran out! The bomb exploded!")
    elif result["answer"] == secret_code:
        remaining = round(time_limit - elapsed, 1)
        print(f"\n✅ DEFUSED! You entered the correct code with {remaining}s to spare!")
    else:
        print(f"\n💥 WRONG CODE! The correct code was {secret_code}. BOOM!")
