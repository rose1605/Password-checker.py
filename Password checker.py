import re


def evaluate_password_strength(password):
    # Criteria checks
    length_check = len(password) >= 8
    lowercase_check = re.search(r"[a-z]", password) is not None
    uppercase_check = re.search(r"[A-Z]", password) is not None
    digit_check = re.search(r"[0-9]", password) is not None
    special_char_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Evaluation of strength based on the number of criteria met
    score = sum([length_check, lowercase_check, uppercase_check, digit_check, special_char_check])

    # Define strength levels
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    print("Password Strength:", strength)
    if not length_check:
        print(" - Password should be at least 8 characters long.")
    if not lowercase_check:
        print(" - Password should include at least one lowercase letter.")
    if not uppercase_check:
        print(" - Password should include at least one uppercase letter.")
    if not digit_check:
        print(" - Password should include at least one digit.")
    if not special_char_check:
        print(" - Password should include at least one special character.")

    return strength


# Example usage
password = input("Enter your password: ")
evaluate_password_strength(password)
