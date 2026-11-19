import random

AUTHOR = "Yugo206"

# Each entry: (email text, True if phishing / False if legitimate)
EMAILS = [
    ("Your bank account will be closed in 24 hours. Click here to verify your details.", True),
    ("Your monthly statement is now available in your online banking portal.", False),
    ("You have won a $1000 gift card! Reply with your credit card number to claim it.", True),
    ("Reminder: your team meeting is scheduled for 10:00 AM tomorrow.", False),
    ("URGENT: Your password expires today. Log in at http://secure-login.example-verify.biz now.", True),
    ("Thanks for your order! Your package has shipped and will arrive on Friday.", False),
    ("Security alert: unusual sign-in detected. Send us your password to restore access.", True),
    ("Your library book is due back next week. You can renew it online.", False),
    ("Final notice: unpaid tax refund. Download the attached file and enter your SSN.", True),
    ("Here are the notes from today's class. Let me know if you have questions.", False),
]


def get_answer(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("p", "phishing"):
            return True
        if answer in ("l", "legit", "legitimate"):
            return False
        print("Please type 'P' for phishing or 'L' for legitimate.")


def run():
    print("Game by", AUTHOR)
    print("\n📧 SUSPICIOUS EMAIL DETECTOR 📧")
    print("Read each email and decide if it is LEGITIMATE or PHISHING.\n")

    rounds = 5
    score = 0
    emails = random.sample(EMAILS, rounds)

    for i, (text, is_phishing) in enumerate(emails, 1):
        print(f"Email {i}/{rounds}:")
        print(f'"{text}"')

        if get_answer("Is this email (P)hishing or (L)egitimate? ") == is_phishing:
            print("✅ Correct!\n")
            score += 1
        else:
            answer = "phishing" if is_phishing else "legitimate"
            print(f"❌ Wrong! This email was {answer}.\n")

    print(f"🏁 Game Over! Your score: {score}/{rounds}")
