import random
import string

def generate_password(length=12, use_special_chars=True):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password = generate_password(length=16)
    print("Generated Password:", password)
