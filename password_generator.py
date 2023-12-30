import random
import string

def generate_password(length=12):
    # Define character sets for the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure password length is at least 4 and contains at least one character from each set
    if length < 4:
        length = 4

    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(special_characters)
        + ''.join(random.choice(all_characters) for _ in range(length - 4))
    )

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
