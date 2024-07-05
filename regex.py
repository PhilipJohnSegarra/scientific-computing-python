import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            #match all digits with \d
            (nums, r'\d'),
            # fr is f and r(raw strings) combined, match symbols with the symbols varible
            (special_chars, fr'[{symbols}]'),
            #match uppercase with character class [A-Z]
            (uppercase, r'[A-Z]'),
            #match lowercase with character class [a-z]
            (lowercase, r'[a-z]')
        ]

        # Check constraints using generator      
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)