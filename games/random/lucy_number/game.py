import random
import time
import os
import sys

AUTHOR = "johannimis"

# ANSI color codes
R      = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
MAGENTA = "\033[95m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"

EVENTS = [
    ("Gold Rush",      "A massive gold vein is discovered in the hills!",      80,  True),
    ("Fierce Storm",   "A fierce storm ravages the entire region!",            -65, False),
    ("Grand Festival", "The kingdom erupts in a grand celebration!",            55,  True),
    ("Plague",         "A mysterious illness spreads through the land!",       -75, False),
    ("Lost Treasure",  "Ancient treasure chests are unearthed at the docks!",  90,  True),
    ("Earthquake",     "The earth trembles and buildings crumble overnight!",  -55, False),
    ("Great Harvest",  "A bountiful harvest fills every granary to the brim!", 50,  True),
    ("Drought",        "Scorching heat withers all the crops for miles!",      -45, False),
    ("Trade Winds",    "Merchants arrive from distant lands bearing riches!",   65,  True),
    ("Bandit Raid",    "Ruthless bandits pillage towns across the land!",      -60, False),
    ("Volcanic Ash",   "A volcano erupts, burying fields in thick ash!",       -80, False),
    ("Lucky Rainbow",  "A magical rainbow arcs over your village!",             70,  True),
    ("Falling Comet",  "A lucky comet streaks across the midnight sky!",        60,  True),
    ("Flash Flood",    "Rising floodwaters sweep away everything below!",      -50, False),
    ("Dragon's Gift",  "A benevolent dragon shares its hoard of gold!",       100,  True),
    ("Solar Eclipse",  "A rare eclipse fills hearts with awe and wonder!",     45,  True),
    ("Locust Swarm",   "Millions of locusts devour the countryside!",          -70, False),
]

ROUNDS = 8


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def type_print(text, delay=0.025):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def proximity(player: int, lucky: int) -> float:
    return 1.0 - abs(player - lucky) / 99.0


def event_delta(base: int, prox: float, good: bool) -> int:
    if good:
        multiplier = 0.10 + prox * 1.90
    else:
        multiplier = 0.15 + (1.0 - prox) * 1.85
    return int(base * multiplier)


def score_bar(score: int, width: int = 28) -> str:
    clamped = max(-500, min(500, score))
    filled = int((clamped + 500) / 1000 * width)
    bar = "█" * filled + "░" * (width - filled)
    color = GREEN if score >= 150 else YELLOW if score >= 0 else RED
    return f"{color}[{bar}]{R}"


def warmth_label(player: int, lucky: int) -> str:
    d = abs(player - lucky)
    if d == 0:   return f"{MAGENTA}{BOLD}★  PERFECT ALIGNMENT  ★{R}"
    if d <= 5:   return f"{RED}Scorching hot!{R}"
    if d <= 12:  return f"{YELLOW}Very warm...{R}"
    if d <= 25:  return f"{CYAN}Lukewarm.{R}"
    if d <= 45:  return f"{BLUE}Cool...{R}"
    return               f"{WHITE}Ice cold.{R}"


def rating(score: int) -> str:
    if score >= 400:  return f"{MAGENTA}{BOLD}LEGENDARY FORTUNE{R}"
    if score >= 200:  return f"{GREEN}{BOLD}Prosperous Run{R}"
    if score >= 50:   return f"{YELLOW}{BOLD}Modest Gains{R}"
    if score >= 0:    return f"{CYAN}{BOLD}Barely Survived{R}"
    return                    f"{RED}{BOLD}Ruined by Misfortune{R}"


def get_player_number() -> int:
    while True:
        try:
            n = int(input(f"\n{BOLD}Choose your number (1 - 100): {R}"))
            if 1 <= n <= 100:
                return n
            print(f"  {RED}Must be between 1 and 100.{R}")
        except ValueError:
            print(f"  {RED}Whole numbers only.{R}")


def print_header():
    clear()
    print(f"{BOLD}{CYAN}")
    print("  ╔══════════════════════════════════════════╗")
    print("  ║       L U C K Y   N U M B E R           ║")
    print("  ║           C H R O N I C L E S           ║")
    print("  ╚══════════════════════════════════════════╝")
    print(R)


def run_game():
    print_header()
    type_print("  A hidden Lucky Number lurks between 1 and 100.", 0.022)
    type_print("  Proximity to it shapes your fate each round.", 0.022)
    type_print("  Survive the events. Uncover the secret.\n", 0.022)

    player = get_player_number()
    lucky  = random.randint(1, 100)
    score  = 0

    print(f"\n  {YELLOW}Your number: {BOLD}{player}{R}")
    print(f"  {CYAN}The lucky number hides in the shadows..{R}\n")
    time.sleep(0.8)

    pool = EVENTS.copy()
    random.shuffle(pool)
    chosen_events = pool[:ROUNDS]

    for i, (name, desc, base, good) in enumerate(chosen_events, 1):
        input(f"  Press {BOLD}ENTER{R} to reveal event {i}/{ROUNDS}...")

        prox  = proximity(player, lucky)
        delta = event_delta(base, prox, good)
        score += delta

        sign  = "+" if delta >= 0 else ""
        color = GREEN if delta >= 0 else RED
        arrow = "▲" if delta >= 0 else "▼"

        print(f"\n  {BOLD}{MAGENTA}{'─'*44}{R}")
        print(f"  {BOLD}{YELLOW}EVENT {i}:{R} {BOLD}{name}{R}")
        print(f"  {desc}")
        print(f"  {BOLD}{MAGENTA}{'─'*44}{R}")
        time.sleep(0.4)

        print(f"\n  {color}{BOLD}{arrow} {sign}{delta} points{R}  |  {warmth_label(player, lucky)}")
        print(f"\n  Score: {score_bar(score)}  {BOLD}{score:+d}{R}\n")
        time.sleep(0.2)

    # ── Final reveal ───────────────────────────────────────────────────
    print(f"\n  {BOLD}{CYAN}{'═'*44}{R}")
    type_print(f"  {BOLD}{CYAN}  THE LUCKY NUMBER WAS...{R}", 0.04)
    time.sleep(1.2)

    print(f"\n        {BOLD}{MAGENTA}✦  ✦  ✦   {lucky}   ✦  ✦  ✦{R}\n")
    time.sleep(0.6)

    dist = abs(player - lucky)
    print(f"  Your number : {BOLD}{player}{R}")
    print(f"  Lucky number: {BOLD}{lucky}{R}")
    print(f"  Distance    : {BOLD}{dist}{R}  |  {warmth_label(player, lucky)}")

    print(f"\n  {BOLD}{'═'*44}{R}")
    print(f"  FINAL SCORE : {BOLD}{score:+d}{R}")
    print(f"  RATING      : {rating(score)}")
    print(f"  {BOLD}{'═'*44}{R}\n")


def run():
    sys.stdout.reconfigure(encoding='utf-8')
    while True:
        run_game()
        again = input(f"  Play again? ({BOLD}y{R}/{BOLD}n{R}): ").strip().lower()
        if again != "y":
            print(f"\n  {CYAN}Thanks for playing Lucky Number Chronicles. Goodbye!{R}\n")
            break
