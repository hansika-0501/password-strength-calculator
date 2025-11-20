import random
import string

def contains_upper(password):
    for ch in password:
        if ch.isupper():
            return True
    return False

def contains_lower(password):
    for ch in password:
        if ch.islower():
            return True
    return False

def contains_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False

def contains_special(password):
    special = "!@#$%^&*(),.?\":{}|<>_+-=[]"
    for ch in password:
        if ch in special:
            return True
    return False


def check_password_strength(password):
    strength_points = 0
    reasons = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
        reasons.append("Length is good")
    else:
        reasons.append(" Length is less than 8")

    # Uppercase check
    if contains_upper(password):
        strength_points += 1
        reasons.append("Contains uppercase letters")
    else:
        reasons.append("Missing uppercase letters")

    # Lowercase check
    if contains_lower(password):
        strength_points += 1
        reasons.append("Contains lowercase letters")
    else:
        reasons.append("Missing lowercase letters")

    # Digit check
    if contains_digit(password):
        strength_points += 1
        reasons.append("Contains numbers")
    else:
        reasons.append("Missing numbers")

    # Special character check
    if contains_special(password):
        strength_points += 1
        reasons.append("Contains special characters")
    else:
        reasons.append("Missing special characters")

    # Strength classification
    if strength_points == 5:
        strength = "STRONG"
    elif strength_points >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return strength, reasons


def generate_strong_password(length=9):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#&*_"
    )
    password = "".join(random.choice(characters) for _ in range(length))
    return password


# --- Main Program ---
user_password = input("Enter your password: ")

strength, details = check_password_strength(user_password)

print("\nPassword Strength:", strength)
print("\nDetails:")
for d in details:
    print(d)

if strength == "WEAK":
    suggestion = generate_strong_password()
    print("\n Your password is WEAK.")
    print(" Suggested Strong Password:", suggestion)

elif strength == "MEDIUM":
    suggestion = generate_strong_password()
    print("\nYour password is MEDIUM.")
    print(" You can use this stronger password:", suggestion)

else:
    print("\n Your password is strong!")
