#  Contributing to Terminal Arcade

Thanks for your interest in contributing!

This project is designed to be simple and beginner-friendly. Please follow the rules below to keep everything clean and working.

---

###  Rules

- Each game must be in its own folder
- Each game must contain a `game.py` file
- Each game must include a `run()` function
- Do NOT print anything when the file is imported
- Keep your code simple and readable

---

###  Project Structure

```
terminal-arcade/
  games/
    category/
      game_name/
        game.py
```

Example:

```
games/
  chill/
    hangman/
      game.py
```

---

###  Game Requirements

Each game must define a `run()` function.

```
def run():
    print("Game starting...")
```

###  Important

- The game must NOT run automatically when imported
- Only execute code inside `run()`
- Do not add unnecessary dependencies

---

###  Author Credit

Each game must include an author:

```
AUTHOR = "your_github_username"
```

Example:

```
AUTHOR = "Yugo206"

def run():
    print(f"Game by {AUTHOR}")
```

---

###  How to Contribute

1. Fork the repository
2. Clone your fork
3. Create a branch:

```
git checkout -b feature/add-your-game
```

4. Add your game in the correct folder  
5. Commit your changes  
6. Open a Pull Request

---

##  Dependencies

By default, games should NOT require external libraries.

If your game needs dependencies:

- Add a `requirements.txt` file inside your game folder
- Keep dependencies minimal
- The launcher will NOT install them automatically

Example:

```
games/chill/mygame/
  game.py
  requirements.txt
```

---

###  Ideas

- Hangman
- Quiz
- Timer
- Calculator
- Mini RPG
- Anything fun!

---

###  Important

- Broken or incomplete games may be rejected  
- Code that does not follow the rules may be rejected

---

Thanks for helping build Terminal Arcade!
