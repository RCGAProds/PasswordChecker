import re


def check_pass_len(password):
    """Check if password is long enough"""
    min_len = 8

    if len(password) < min_len:
        return False, f"❌ Password too short, minimum {min_len} characters."
    else:
        return True, f"✔️ Good length ({len(password)} characters)."


def check_uppercase(password):
    """Check for uppercase chars"""

    if bool(re.search(r"[A-Z]", password)):
        return True, "✔️ Contains uppercase letters"
    else:
        return False, "❌ Add uppercase letters"


def check_lowercase(password):
    """Check for lowercase chars"""

    if bool(re.search(r"[a-z]", password)):
        return True, "✔️ Contains lowercase letters"
    else:
        return False, "❌ Add lowercase letters"


def check_digit(password):
    """Check for digits chars"""

    if bool(re.search(r"\d", password)):
        return True, "✔️ Contains numbers"
    else:
        return False, "❌ Add numbers"


def check_special(password):
    """Check for special chars"""

    if bool(re.search(r"[!*@%#$^&]", password)):
        return True, "✔️ Contains special characters"
    else:
        return False, "❌ Add special characters"


def get_rating(score):
    """Get strength rating based on the score"""
    if score <= 1:
        return "❌❌❌ Extremely Weak ❌❌❌"
    elif score <= 2:
        return "❌❌ Very Weak ❌❌"
    elif score <= 3:
        return "❌ Weak ❌"
    elif score <= 4:
        return "⚠️ Poor ⚠️"
    else:
        return "✔️ Strong ✔️"


def is_common_password(password):
    """Check if password is commonly used"""
    common = ["password", "admin", "user", "12345", "54321", "qwerty"]
    return password.lower() in common


def calculate_score(password):
    """Calculate password strength score, with feedback and rating"""

    score = 0
    feedback = []

    # Check if its a common password
    if is_common_password(password):
        return 0, ["❌❌❌ CRITICAL: This is a common password!!! ❌❌❌"]

    # Checks
    checks = [
        check_pass_len,
        check_uppercase,
        check_lowercase,
        check_digit,
        check_special,
    ]

    for check in checks:
        valid, msg = check(password)

        if valid:
            score += 1

        feedback.append(msg)

    rating = get_rating(score)

    return score, feedback, rating


def display_results(password, score, feedback, rating):
    """Display results"""
    print("-" * 20)
    print("  PASSWORD CHECKER")
    print("-" * 20)

    print(f"Password: {'*' * len(password)}")
    print(f"Score: {score}/5")
    print(f"Rating: {rating}")
    print(f"\nFeedback:")
    for msg in feedback:
        print(f"    {msg}")
    print("-" * 20)


def main():
    """Main Password Checker Application"""
    print("\nWelcome to Password Checker!")
    print("Type 'q' to exit\n")

    while True:
        password = input("Enter a password: ")

        if password.lower() == "q":
            print("🔒 Goodbye, Stay Secure! 🔒\n")
            break

        if not password:
            print("❌ Please enter a password. ❌\n")
            continue

        score, feedback, rating = calculate_score(password)
        display_results(password, score, feedback, rating)


if __name__ == "__main__":
    main()
