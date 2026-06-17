AUTHOR = "Yugo206"

import time
import random

# Pool of funny tasks and results grouped by categories (At least 15 required, 18 detailed here + custom ones)
LOADING_TASKS = {
    "system": [
        {"task": "Installing Happiness v2.0", "result": "❌ FAILED: Dependency 'Money' (>= $1,000,000) not found."},
        {"task": "Downloading Common Sense", "result": "⚠️ ERROR: Target device architecture is not compatible."},
        {"task": "Simulating 'Adulting' module", "result": "💥 CRITICAL FAILURE: Unexpected bills. Please reboot in child mode."},
        {"task": "Deleting Childhood Trauma", "result": "🔒 ACCESS DENIED: File currently in use by 'Brain'."},
        {"task": "Updating Bank Balance", "result": "💳 COMPLETED: Current balance is $0.03. Please deposit more hope."},
        {"task": "Locating Self-Control (Snack edition)", "result": "🍩 NOT FOUND: Sweets detected. System bypass active."}
    ],
    "work": [
        {"task": "Searching for Motivation", "result": "🔍 404 NOT FOUND: Motivation has left the building. Try looking in bed."},
        {"task": "Compiling bug-free code", "result": "👾 WARNING: Compilation succeeded, but logic makes absolutely no sense."},
        {"task": "Gathering will to exercise", "result": "🛋️ TIMEOUT: Connection reset by Couch (IP: 127.0.0.1)."},
        {"task": "Calculating optimal life choices", "result": "📈 CRASHED: Stack overflow on regret. Please consult your cat."},
        {"task": "Analyzing productivity levels", "result": "☕ FAILED: Insufficient coffee intake detected."},
        {"task": "Loading creative thinking module", "result": "🖥️ STANDBY: Brain is currently staring at a blank wall."}
    ],
    "social": [
        {"task": "Locating Social Skills", "result": "🤐 TIMEOUT: Server did not respond. Initiating awkward silence."},
        {"task": "Generating appropriate responses (Filter.exe)", "result": "💥 CRITICAL ERROR: Filter.exe crashed. Sarcasm overflow!"},
        {"task": "Activating personal Charisma", "result": "👔 FAILED: Signal strength too low. Please change outfit and try again."},
        {"task": "Synchronizing brain with mouth", "result": "🚫 BLOCKED: Words spoken before thinking process finished."},
        {"task": "Cleaning browser search history", "result": "🔥 COMPLETED: 8,742 items incinerated. You are safe... for now."},
        {"task": "Processing compliments from others", "result": "⚠️ UNHANDLED EXCEPTION: System panicked. Response was 'You too'."}
    ]
}

GENERIC_RESULTS = [
    "❌ FAILED: Target ignored all instructions.",
    "⚠️ SUCCESS... just kidding, it crashed.",
    "🚫 BLOCKED: Because why would anything work today?",
    "💥 ERROR: Insufficient brain cells to complete action.",
    "⏳ TIMEOUT: User got distracted by a shiny object.",
    "🛑 ABORTED: The universe decided against this.",
    "✔️ COMPLETED: But you will highly regret the outcome."
]

SPEEDS = {
    "1": ("Quantum (Instant)", 0.05),
    "2": ("Fiber (Fast)", 0.4),
    "3": ("Broadband (Normal)", 1.0),
    "4": ("56k Dial-Up (Painfully Slow)", 3.0)
}


def draw_progress_bar(task_name, speed_multiplier):
    print(f"\n⚙️  {task_name}")
    bar_width = 40
    i = 0
    
    # Stalls represent funny realistic loading barriers
    stall_points = {
        random.randint(20, 45): random.uniform(0.4, 1.0) * speed_multiplier, 
        99: random.uniform(1.0, 2.5) * speed_multiplier
    }
    
    while i <= bar_width:
        percent = int((i / bar_width) * 100)
        filled = "█" * i
        empty = "░" * (bar_width - i)
        spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"][i % 10]
        
        print(f"\r  {spinner} [{filled}{empty}] {percent}%", end="", flush=True)
        
        # Determine delay
        delay = random.uniform(0.02, 0.08) * speed_multiplier
        if percent in stall_points:
            time.sleep(stall_points[percent])
        else:
            time.sleep(delay)
        i += 1
    print()


def simulate_dialup():
    print("\n[!] Initializing phone line handshake...")
    time.sleep(0.8)
    handshakes = [
        "📞 Dialing 01904 425232...",
        "🔊 *BEEP BOOP SKRRRRR*",
        "🔊 *KZZZZZT CHRRRRRR*",
        "🔊 *DING DONG DING BEEP*",
        "✔️ Connected at 28.8 Kbps!"
    ]
    for step in handshakes:
        print(f"  {step}")
        time.sleep(0.7)
    time.sleep(0.5)


def run():
    speed_option = "3"  # Default is Broadband (Normal)

    print("==================================================")
    print("         ⚡ FAKE LOADING SIMULATOR ⚡             ")
    print("==================================================")
    print("Need to look busy? Or just want a quick laugh?")
    print("Welcome to the ultimate Loading Simulator!")
    print("==================================================")
    time.sleep(0.8)

    while True:
        current_speed_name = SPEEDS[speed_option][0]
        print("\n=== SIMULATOR CONTROLS ===")
        print(f"Connection Speed: {current_speed_name}")
        print("--------------------------")
        print("1. Load System/Life Diagnostics")
        print("2. Load Productivity & Work Modules")
        print("3. Load Personality & Social Skills")
        print("4. Load Random Diagnostic Batch")
        print("5. Run Custom Loading Task")
        print("6. Change Connection Speed")
        print("7. Exit Simulator")

        choice = input("\nChoose an option: ").strip()

        if choice == "7":
            print("\nShutting down loader... System idle.")
            print("==================================================")
            return

        speed_multiplier = SPEEDS[speed_option][1]

        if choice in ["1", "2", "3"]:
            category = "system" if choice == "1" else ("work" if choice == "2" else "social")
            selected = random.choice(LOADING_TASKS[category])
            
            if speed_option == "4":
                simulate_dialup()

            draw_progress_bar(selected["task"], speed_multiplier)
            time.sleep(0.5)
            print("\nResult:")
            print(f"  {selected['result']}")
            print("-" * 50)
            input("\nPress ENTER to continue...")

        elif choice == "4":
            # Select random task from any category
            all_tasks = LOADING_TASKS["system"] + LOADING_TASKS["work"] + LOADING_TASKS["social"]
            selected = random.choice(all_tasks)

            if speed_option == "4":
                simulate_dialup()

            draw_progress_bar(selected["task"], speed_multiplier)
            time.sleep(0.5)
            print("\nResult:")
            print(f"  {selected['result']}")
            print("-" * 50)
            input("\nPress ENTER to continue...")

        elif choice == "5":
            custom_task = input("\nEnter name of custom task to load: ").strip()
            if not custom_task:
                print("❌ Task name cannot be empty.")
                continue

            if speed_option == "4":
                simulate_dialup()

            draw_progress_bar(custom_task, speed_multiplier)
            time.sleep(0.5)
            result = random.choice(GENERIC_RESULTS)
            print("\nResult:")
            print(f"  {result}")
            print("-" * 50)
            input("\nPress ENTER to continue...")

        elif choice == "6":
            print("\n--- SELECT CONNECTION SPEED ---")
            for k, v in SPEEDS.items():
                print(f"{k}. {v[0]}")
            
            new_speed = input("\nSelect speed option (1-4): ").strip()
            if new_speed in SPEEDS:
                speed_option = new_speed
                print(f"✔️ Speed changed to: {SPEEDS[speed_option][0]}")
            else:
                print("❌ Invalid speed option.")
            time.sleep(0.5)

        else:
            print("❌ Invalid option. Please select between 1 and 7.")
            time.sleep(0.5)
