import random
import string

def password_generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters

    if numbers:
        character += digits
    if special_characters:
        character += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria:
        pwd = ""

        for _ in range(min_length):
            pwd += random.choice(character)
            # print(pwd) # Optional: uncomment if you want to see progress

        if numbers:
            has_number = any(char in digits for char in pwd)
        else:
            has_number = True

        if special_characters:
            has_special = any(char in special for char in pwd)
        else:
            has_special = True

        # Fixed: now correctly checks both number and special character criteria
        meets_criteria = has_number and has_special

    return pwd




# Get user input

min_length = int(input("Enter minimum password length: "))

has_numbers = input("Include numbers? (y/n): ").lower() == "y"

has_special = input("Include special characters? (y/n): ").lower() == "y"


# Generate password

password = password_generator(min_length, has_numbers, has_special)


print("Generated Password:", password)