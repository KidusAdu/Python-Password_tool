
import string
import secrets


# Common passwords that should be avoided
COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
}


def check_password(password):
    """Check a password against several basic security rules."""

    score = 0
    feedback = []

    # Rule 1: Check the password length
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Rule 2: Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter (a-z).")

    # Rule 3: Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter (A-Z).")

    # Rule 4: Check for numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number (0-9).")

    # Rule 5: Check for special symbols
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special symbol, such as ! or #.")

    # Rule 6: Check a small list of common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a common password. Avoid it.")

    # Show the result
    if password.lower() in COMMON_PASSWORDS:
        strength = "WEAK"
    elif score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    print("\n--- Password Check Result ---")
    print("Strength:", strength)
    print("Rules passed:", score, "out of 5")

    if feedback:
        print("\nSuggestions:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("Your password passed all five basic checks!")

    print("\nRemember: this is a basic checker, not a guarantee "
          "that a password is secure.")


def generate_password(length):
    """Generate a random password with all four character types."""

    if length < 12:
        raise ValueError("Choose a password length of at least 12.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Select at least one character from each group
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(symbols),
    ]

    # Fill the remaining positions with random characters
    all_characters = lowercase + uppercase + numbers + symbols

    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_characters))

    # Randomize the order of all characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    """Display the menu and let the user choose a tool."""

    while True:
        print("\n===== PASSWORD SECURITY TOOLKIT =====")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            password = input("Enter a test password: ")
            check_password(password)

        elif choice == "2":
            try:
                length = int(input("Enter password length (12 or more): "))

                password = generate_password(length)

                print("\nGenerated password:", password)
                print("Store it securely and do not share it.")

            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "3":
            print("Thank you for using the Password Security Toolkit!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
