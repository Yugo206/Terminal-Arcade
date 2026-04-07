import random


AUTHOR = "Bhanu-inturi"


def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operations)

    question = f"{num1} {op} {num2}"

    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return question, answer


def run():
    print("Game by ", AUTHOR)
    print("🎮 Welcome to the Calculator Game!")
    print("Solve the math problems.\n")

    score = 0
    rounds = 5

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"Question {i+1}: {question}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("❌ Invalid input! Skipping question.\n")
            continue

        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was {correct_answer}\n")

    print(f"🏁 Game Over! Your score: {score}/{rounds}")
