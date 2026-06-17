AUTHOR = "Yugo206"

import time
import random

# ASCII Art for Chest Stages
CLOSED_CHEST = r"""
        .=================.
       /                 /|
      /_________________/ |
      |                 | |
      |     [═ 🔒 ═]    | /
      |_________________|/
"""

OPENING_CHEST = r"""
           .=========.
          /         /|
         /_________/ /
        /_________/ /
       |          |/
       |  [═ 🔓 ═] |/
       |__________|
"""

OPEN_CHEST = r"""
           .=========.
          /         /|
         /_________/ /
        / ✨  ✨  / /
       |  🌟  🌟  |/
       |  [═ 🎁 ═] |/
       |__________|
"""

# Pool of 18 unique rewards (At least 10 required)
REWARDS = {
    "gold": [
        {"name": "a Small Coin Purse", "desc": "You found a leather purse stuffed with a few gold coins.", "val": 25},
        {"name": "a Merchant's Gold Sack", "desc": "A heavy sack of shiny gold coins. Smells like success!", "val": 75},
        {"name": "an Ancient Dwarven Treasure", "desc": "Engraved gold bars from an ancient dwarven hoard.", "val": 150},
        {"name": "a Royal King's Ransom", "desc": "A legendary chest of royal gold, sparkling with wealth!", "val": 350}
    ],
    "legendary": [
        {"name": "⚔️ Excalibur", "desc": "The mythical sword of King Arthur, glowing with pure holy light."},
        {"name": "🛡️ Aegis Shield", "desc": "The legendary shield of Athena, showing a faint glow of protection."},
        {"name": "⚡ Mjolnir", "desc": "The mighty hammer of Thor, crackling with raw static electricity."},
        {"name": "🔮 Philosopher's Stone", "desc": "A crimson gem believed to turn metals to gold and grant eternal life."},
        {"name": "🧥 Cloak of Invisibility", "desc": "A silky, fluid cloak that bends light around you completely."},
        {"name": "💍 Ring of Power", "desc": "One Ring to rule them all... it whispers dark secrets to you."}
    ],
    "nothing": [
        {"name": "Empty Air", "desc": "You open it, but a cold gust of wind is all that greets you."},
        {"name": "Cobwebs & Dust", "desc": "Nothing but thick cobwebs and a cloud of dust that makes you cough."},
        {"name": "a Friendly Spider", "desc": "A tiny spider crawls out, waves its legs at you, and runs away."},
        {"name": "a Mocking Note", "desc": "A small slip of paper inside says: 'Thank you! But your treasure is in another chest.'"}
    ],
    "trap": [
        {"name": "Mimic Bite", "desc": "The chest grows sharp teeth and bites your hand! Ouch!", "damage": 25},
        {"name": "Poison Gas", "desc": "A green cloud of toxic gas bursts out of the lock! You inhale the fumes.", "damage": 15},
        {"name": "Explosive Rune", "desc": "A magic rune flashes red and explodes right in your face!", "damage": 40},
        {"name": "Dart Trap", "desc": "A pressure plate triggers, firing a poison dart into your shoulder!", "damage": 20}
    ]
}


def print_loading(message, duration=3):
    print(message, end="", flush=True)
    for _ in range(duration):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()


def animate_opening():
    print(CLOSED_CHEST)
    time.sleep(0.6)
    print_loading("\n[!] Turning key, mechanism clicking", 3)
    print(OPENING_CHEST)
    time.sleep(0.6)
    print_loading("\n[!] Lifting the heavy lid", 2)
    print(OPEN_CHEST)
    time.sleep(0.6)


def run():
    # Initialize game state
    health = 100
    gold = 50
    inventory = []
    
    keys = {
        "common": 2,
        "rare": 1,
        "epic": 0
    }

    print("==================================================")
    print("        💰  TREASURE CHEST OPENING GAME  💰        ")
    print("==================================================")
    print("Welcome, Adventurer! You have entered the dungeon.")
    print("Your goal is to gather as much Gold and collect as")
    print("many Legendary Items as you can without dying to traps.")
    print("==================================================")
    time.sleep(1.0)

    while True:
        # Check health
        if health <= 0:
            print("\n💀💀💀 GAME OVER 💀💀💀")
            print("You ran out of health and collapsed in the dungeon!")
            print(f"Total Gold Lost: {gold}")
            if inventory:
                print("The legendary items you dropped:")
                for item in inventory:
                    print(f" - {item}")
            else:
                print("You didn't find any legendary items.")
            print("Better luck next time, brave explorer!")
            print("==================================================")
            return

        # Main HUD
        print("\n=== CHARACTER STATUS ===")
        print(f"❤️  Health: {health}/100 HP")
        print(f"💰  Gold: {gold} G")
        print(f"🔑  Keys: {keys['common']} Common, {keys['rare']} Rare, {keys['epic']} Epic")
        print(f"🏆  Legendary Items: {len(inventory)}")
        print("========================")
        print("1. Open a Chest")
        print("2. Visit the Mystic Shop")
        print("3. View Inventory & Stats")
        print("4. Read Game Rules / Guide")
        print("5. Cash Out & Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            print("\n--- CHOOSE A CHEST ---")
            print(f"1. Rusted Lockbox (Costs 15 Gold directly)")
            print(f"2. Wooden Chest   (Requires 1 Common Key | Current: {keys['common']})")
            print(f"3. Iron Chest     (Requires 1 Rare Key   | Current: {keys['rare']})")
            print(f"4. Golden Chest   (Requires 1 Epic Key   | Current: {keys['epic']})")
            print("5. Back to Main Menu")

            chest_choice = input("\nWhich chest do you want to open? ").strip()

            if chest_choice == "5":
                continue

            # Validate cost/keys
            chest_type = None
            if chest_choice == "1":
                if gold < 15:
                    print("\n❌ You do not have enough Gold (15 G required).")
                    continue
                gold -= 15
                chest_type = "lockbox"
            elif chest_choice == "2":
                if keys["common"] < 1:
                    print("\n❌ You do not have a Common Key.")
                    continue
                keys["common"] -= 1
                chest_type = "wooden"
            elif chest_choice == "3":
                if keys["rare"] < 1:
                    print("\n❌ You do not have a Rare Key.")
                    continue
                keys["rare"] -= 1
                chest_type = "iron"
            elif chest_choice == "4":
                if keys["epic"] < 1:
                    print("\n❌ You do not have an Epic Key.")
                    continue
                keys["epic"] -= 1
                chest_type = "golden"
            else:
                print("\n❌ Invalid choice.")
                continue

            # Animate chest opening
            animate_opening()

            # Determine outcome category based on chest type
            # Categories: trap, nothing, gold, legendary
            roll = random.random()
            outcome_category = ""

            if chest_type == "lockbox":
                # 15% Trap, 45% Nothing, 38% Gold, 2% Legendary
                if roll < 0.15:
                    outcome_category = "trap"
                elif roll < 0.60:
                    outcome_category = "nothing"
                elif roll < 0.98:
                    outcome_category = "gold"
                else:
                    outcome_category = "legendary"

            elif chest_type == "wooden":
                # 10% Trap, 35% Nothing, 50% Gold, 5% Legendary
                if roll < 0.10:
                    outcome_category = "trap"
                elif roll < 0.45:
                    outcome_category = "nothing"
                elif roll < 0.95:
                    outcome_category = "gold"
                else:
                    outcome_category = "legendary"

            elif chest_type == "iron":
                # 15% Trap, 20% Nothing, 55% Gold, 10% Legendary
                if roll < 0.15:
                    outcome_category = "trap"
                elif roll < 0.35:
                    outcome_category = "nothing"
                elif roll < 0.90:
                    outcome_category = "gold"
                else:
                    outcome_category = "legendary"

            elif chest_type == "golden":
                # 20% Trap, 10% Nothing, 50% Gold, 20% Legendary
                if roll < 0.20:
                    outcome_category = "trap"
                elif roll < 0.30:
                    outcome_category = "nothing"
                elif roll < 0.80:
                    outcome_category = "gold"
                else:
                    outcome_category = "legendary"

            # Draw the specific reward from the category
            reward_pool = REWARDS[outcome_category]
            reward = random.choice(reward_pool)

            print("\n" + "=" * 40)
            if outcome_category == "trap":
                damage = reward["damage"]
                health -= damage
                print(f"⚠️  TRAP ENCOUNTERED: {reward['name']}!")
                print(f"{reward['desc']}")
                print(f"💔 You took {damage} damage!")
            elif outcome_category == "nothing":
                print(f"💨 NOTHING INSIDE: {reward['name']}")
                print(f"{reward['desc']}")
            elif outcome_category == "gold":
                earned = reward["val"]
                # Add a bit of randomness to the gold value
                earned_actual = int(earned * random.uniform(0.8, 1.2))
                gold += earned_actual
                print(f"💰 GOLD FOUND: {reward['name']}!")
                print(f"{reward['desc']}")
                print(f"✨ You gathered +{earned_actual} Gold!")
            elif outcome_category == "legendary":
                item_name = reward["name"]
                if item_name in inventory:
                    # Duplicate item gets converted to gold
                    comp_gold = 100
                    gold += comp_gold
                    print(f"🏆 DUPLICATE LEGENDARY: {item_name}!")
                    print(f"You already own this. It has been sold to merchants for +{comp_gold} Gold!")
                else:
                    inventory.append(item_name)
                    print(f"🌟 LEGENDARY ITEM ACQUIRED: {item_name}!")
                    print(f"{reward['desc']}")
                    print("This artifact is now safely stored in your inventory.")
            print("=" * 40)
            input("\nPress ENTER to continue...")

        elif choice == "2":
            while True:
                print("\n--- MYSTIC MERCHANT SHOP ---")
                print(f"Current Gold: {gold} G | Health: {health}/100 HP")
                print("----------------------------")
                print("1. Buy Common Key (30 Gold)")
                print("2. Buy Rare Key   (75 Gold)")
                print("3. Buy Epic Key   (150 Gold)")
                print("4. Buy Healing Potion (+30 HP | Costs 40 Gold)")
                print("5. Buy Elixir of Life (Heal to Full HP | Costs 100 Gold)")
                print("6. Exit Shop")

                shop_choice = input("\nWhat would you like to buy? ").strip()

                if shop_choice == "6":
                    break

                if shop_choice == "1":
                    if gold >= 30:
                        gold -= 30
                        keys["common"] += 1
                        print("\n✔️ Purchased 1 Common Key!")
                    else:
                        print("\n❌ Not enough Gold.")
                elif shop_choice == "2":
                    if gold >= 75:
                        gold -= 75
                        keys["rare"] += 1
                        print("\n✔️ Purchased 1 Rare Key!")
                    else:
                        print("\n❌ Not enough Gold.")
                elif shop_choice == "3":
                    if gold >= 150:
                        gold -= 150
                        keys["epic"] += 1
                        print("\n✔️ Purchased 1 Epic Key!")
                    else:
                        print("\n❌ Not enough Gold.")
                elif shop_choice == "4":
                    if health >= 100:
                        print("\n❌ You are already at full Health.")
                    elif gold >= 40:
                        gold -= 40
                        health = min(100, health + 30)
                        print(f"\n✔️ Drank a Healing Potion! HP is now {health}/100.")
                    else:
                        print("\n❌ Not enough Gold.")
                elif shop_choice == "5":
                    if health >= 100:
                        print("\n❌ You are already at full Health.")
                    elif gold >= 100:
                        gold -= 100
                        health = 100
                        print(f"\n✔️ Drank an Elixir of Life! HP is now {health}/100.")
                    else:
                        print("\n❌ Not enough Gold.")
                else:
                    print("\n❌ Invalid choice.")
                
                time.sleep(0.5)

        elif choice == "3":
            print("\n=====================================")
            print("        🎒 CHARACTER DETAILS 🎒      ")
            print("=====================================")
            print(f"❤️  Health Status: {health}/100 HP")
            print(f"💰  Wallet Balance: {gold} Gold")
            print(f"🔑  Keyring: {keys['common']} Common, {keys['rare']} Rare, {keys['epic']} Epic")
            print("\n🏆 COLLECTED LEGENDARY ITEMS:")
            if inventory:
                for i, item in enumerate(inventory, 1):
                    print(f" {i}. {item}")
            else:
                print(" (No legendary items found yet. Keep searching!)")
            print("=====================================")
            input("\nPress ENTER to return to menu...")

        elif choice == "4":
            print("\n=======================================================")
            print("                📖 DUNGEON GUIDE & RULES               ")
            print("=======================================================")
            print("1. Objective: Collect rare legendary items and gold.")
            print("2. Chests require keys to unlock. Higher tier chests")
            print("   have much better odds of yielding legendary items.")
            print("3. Trap hazards: Traps deplete your HP. If your HP")
            print("   hits 0, you die and lose all your gathered loot!")
            print("4. Shop: Use gold earned from chests to purchase keys")
            print("   or heal your health at the Mystic Merchant.")
            print("5. Cash Out: You can leave the dungeon at any time")
            print("   using option 5 to secure your gold and items.")
            print("=======================================================")
            input("\nPress ENTER to return to menu...")

        elif choice == "5":
            print("\n=======================================================")
            print("🎉 Congratulations! You have successfully escaped! 🎉")
            print("=======================================================")
            print("You retired from dungeon crawling with the following loot:")
            print(f"💰 Gold Secured: {gold}")
            print(f"🏆 Legendary Artifacts Found: {len(inventory)}")
            if inventory:
                for item in inventory:
                    print(f" - {item}")
            else:
                print(" - None")
            print("\nThank you for playing! Come back to the dungeon soon!")
            print("=======================================================")
            return
        else:
            print("\n❌ Invalid option. Please enter a number between 1 and 5.")
            time.sleep(0.5)
