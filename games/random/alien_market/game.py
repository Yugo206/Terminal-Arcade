"""
Alien Market Trading
--------------------
Buy strange goods from an alien trader, gamble on holding them, then sell
when the price swings your way. Reach the target credits before you go
bankrupt or run out of rounds.
"""

import random

AUTHOR = "adjenk"
START_CREDITS = 150
TARGET_CREDITS = 500
MAX_ROUNDS = 30

CARGO_CAPACITY = 3  # how many stacks you can hold in cargo at once
MAX_STACK_QTY = 5   # max units bought into a single cargo slot at once

# --- Color palette (plain ANSI escape codes, no external deps) ---
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
GREY = "\033[90m"


def c(text, color):
    """Wrap text in a color code, resetting after."""
    return f"{color}{text}{RESET}"


def clamp_int(x):
    return int(max(0, round(x)))


# Each item has its own price tier and its own risk profile, so the letter
# you pick is a real decision: cheap goods are safer with modest swings,
# rare/expensive goods are volatile with much bigger swings either way.
ITEM_CATALOG = [
    {"name": "Xeno-Fruit",       "buy_range": (10, 18),  "margin_range": (-0.20, 0.35)},
    {"name": "Cryo-Seed",        "buy_range": (18, 30),  "margin_range": (-0.30, 0.55)},
    {"name": "Nebula Thread",    "buy_range": (28, 45),  "margin_range": (-0.35, 0.75)},
    {"name": "Grav-Mint Spice",  "buy_range": (40, 65),  "margin_range": (-0.40, 0.95)},
    {"name": "Void Quartz",      "buy_range": (55, 85),  "margin_range": (-0.45, 1.15)},
    {"name": "Molybdenum Bloom", "buy_range": (75, 115), "margin_range": (-0.50, 1.40)},
]
NUM_ITEMS = 3  # must not exceed len(ITEM_CATALOG), since items can't repeat

# --- ANSI-art title banner (each row its own color, plus a starry border) ---
BANNER_ROWS = [
    r"     _    _ _               __   __            _        _   ",
    r"    / \  | (_) ___ _ __     |  \/  | __ _ _ __| | _____| |_ ",
    r"   / _ \ | | |/ _ \ '_ \    | |\/| |/ _` | '__| |/ / _ \ __|",
    r"  / ___ \| | |  __/ | | |   | |  | | (_| | |  |   <  __/ |_ ",
    r" /_/   \_\_|_|\___|_| |_|   |_|  |_|\__,_|_|  |_|\_\___|\__|",
]
BANNER_GRADIENT = [MAGENTA, BLUE, CYAN, GREEN, YELLOW]
BORDER_COLORS = [MAGENTA, CYAN, YELLOW, GREEN]


def render_banner():
    width = max(len(row) for row in BANNER_ROWS)
    border = "".join(
        c("·", BORDER_COLORS[i % len(BORDER_COLORS)]) for i in range(width)
    )
    lines = [border]
    for row, color in zip(BANNER_ROWS, BANNER_GRADIENT):
        lines.append(c(row, color + BOLD))
    lines.append(border)
    return "\n".join(lines)


INTRO_TEXT = (
    "A rickety alien freighter drifts into dock, cargo bay humming with\n"
    "goods no human has named yet. The trader doesn't speak your language,\n"
    "but credits are credits everywhere in the galaxy.\n\n"
    "Buy low, hold your nerve, and sell high before you're stranded broke\n"
    "on this side of the void."
)


def make_market():
    catalog_items = random.sample(ITEM_CATALOG, NUM_ITEMS)
    items = []
    for i, entry in enumerate(catalog_items):
        item_id = chr(ord("A") + i)
        buy_price = random.randint(*entry["buy_range"])
        items.append({
            "id": item_id,
            "name": entry["name"],
            "buy": buy_price,
            "margin_range": entry["margin_range"],
        })
    return items


def choose(prompt, valid_set, hint=None):
    while True:
        ans = input(prompt).strip().upper()
        if ans in valid_set:
            return ans
        msg = "Invalid choice."
        if hint:
            msg += f" {hint}"
        print(c(msg, RED))


def update_cargo_prices(owned):
    """Roll this round's per-unit sell price for every held stack, visible before deciding."""
    for held in owned:
        margin = random.uniform(*held["margin_range"])
        unit_price = clamp_int(held["buy_price"] * (1 + margin))
        held["current_margin"] = margin
        held["current_unit_price"] = unit_price
        held["current_total_price"] = unit_price * held["qty"]


def print_cargo(owned):
    print(c(f"\n=== Cargo Bay ({len(owned)}/{CARGO_CAPACITY}) ===", CYAN + BOLD))
    if not owned:
        print(c("(empty)", GREY))
        return
    for slot_num, held in enumerate(owned, start=1):
        qty = held["qty"]
        margin = held.get("current_margin")
        total_price = held.get("current_total_price")
        bought_total = held["buy_price"] * qty
        if total_price is None:
            sell_info = c("Sell now: price updates next round", GREY)
        else:
            price_color = GREEN if margin >= 0 else RED
            sell_info = f"Sell now: {c(total_price, price_color)} total ({margin*100:+.1f}%)"
        print(
            f"{c(slot_num, MAGENTA)}. {qty}x {held['item']['name']} "
            f"| Bought for {c(bought_total, YELLOW)} total ({held['buy_price']} each) | {sell_info}"
        )


def make_progress_bar(current, target, width=20):
    filled = int(width * max(0, min(current, target)) / target)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def print_status_bar(round_num, credits, owned):
    if credits >= TARGET_CREDITS * 0.75:
        credit_color = GREEN
    elif credits >= START_CREDITS:
        credit_color = YELLOW
    else:
        credit_color = RED

    bar = make_progress_bar(credits, TARGET_CREDITS)
    status = (
        f"Round {round_num}/{MAX_ROUNDS} "
        f"Credits: {credits}/{TARGET_CREDITS} {bar}  "
        f"Cargo: {len(owned)}/{CARGO_CAPACITY}"
    )
    print(c(status, credit_color + BOLD))


def run():
    credits = START_CREDITS
    round_num = 1

    owned = []  # list of {"item": ..., "buy_price": ..., "qty": ..., "round_bought": ...}

    print(render_banner())
    print()
    print(c(INTRO_TEXT, GREY))
    print()
    print(f"Start credits: {c(START_CREDITS, YELLOW)}")
    print(f"Target: {c(TARGET_CREDITS, GREEN)}")
    print(f"Cargo capacity: {c(CARGO_CAPACITY, YELLOW)} stack(s), up to {MAX_STACK_QTY} units each")
    print("Sell later for profit (or loss). Prices change each round.")

    while True:
        if credits >= TARGET_CREDITS:
            print(c(f"\nYou win! Credits: {credits} (reached target).", GREEN + BOLD))
            return
        if credits <= 0:
            print(c("\nYou went bankrupt. Game over.", RED + BOLD))
            return
        if round_num > MAX_ROUNDS:
            print(c(f"\nOut of time! Final credits: {credits} (needed {TARGET_CREDITS}).", RED + BOLD))
            return

        market = make_market()
        update_cargo_prices(owned)

        print()
        print_status_bar(round_num, credits, owned)

        print(c("\n=== Market ===", CYAN + BOLD))
        for itm in market:
            print(f"{c(itm['id'], MAGENTA)}. {itm['name']} - Buy: {c(itm['buy'], YELLOW)} credits")

        print_cargo(owned)

        # Build this round's menu: buy (if room), sell (if holding anything), or skip
        can_buy = len(owned) < CARGO_CAPACITY
        market_ids = [it["id"] for it in market]
        slot_nums = [str(n) for n in range(1, len(owned) + 1)]

        options = (market_ids if can_buy else []) + slot_nums + ["S"]

        print("\nChoose an option:")
        if can_buy:
            print("- Enter item letter to BUY (auto-buys as many as you can afford)")
        else:
            print(c("- Cargo bay is full — sell something before you can buy", GREY))
        if owned:
            print("- Enter cargo bay number to SELL")
        print("- S to SKIP (hold everything as-is)")

        hint = None
        if not can_buy:
            hint = "Cargo bay is full — sell a slot number before you can buy again."
        choice = choose("> ", set(options), hint=hint)

        if choice == "S":
            print(c("You hold everything as-is for another round.", GREY))
        elif choice in slot_nums:
            slot_index = int(choice) - 1
            held = owned.pop(slot_index)
            margin = held["current_margin"]
            sell_price = held["current_total_price"]
            credits += sell_price

            outcome_color = GREEN if margin >= 0 else RED
            outcome = "PROFIT" if margin >= 0 else "LOSS"
            print(f"\nYou sold {held['qty']}x {held['item']['name']}!")
            print(c(f"Profit margin: {margin*100:.1f}%", outcome_color))
            print(c(f"Received: {sell_price} credits ({outcome})", outcome_color + BOLD))
        else:
            chosen = next(it for it in market if it["id"] == choice)
            price = chosen["buy"]
            spendable = int(credits * 0.8)
            qty = min(MAX_STACK_QTY, spendable // price)
            if qty < 1:
                print(c("Not enough credits to buy even one unit of that item.", RED))
            else:
                cost = price * qty
                credits -= cost
                owned.append({
                    "item": chosen,
                    "buy_price": price,
                    "qty": qty,
                    "margin_range": chosen["margin_range"],
                    "round_bought": round_num,
                })
                print(c(f"Bought {qty}x {chosen['name']} for {cost} credits ({price} each).", GREEN))

        round_num += 1


