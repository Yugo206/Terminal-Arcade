import random
import string

def generate_password(length: int) -> str:
    """Generate a random password of the given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def run():
    Length = int(input("Enter the desired password length: "))
    password = generate_password(Length)
    print(f"Generated password: {password}")
