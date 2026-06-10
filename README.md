# PasswordChecker

A simple CLI tool written in Python to evaluate password strength. Zero external dependencies — uses only the Python standard library.

## Features

- 6 security checks: length (≥8), uppercase, lowercase, digits, special characters, common-password blacklist
- Score from 0 to 5 with a descriptive rating
- Detailed per-criterion feedback
- Interactive REPL loop
- No third-party dependencies

## Requirements

- Python 3.6+

## Installation

```bash
git clone https://github.com/RCGAProds/PasswordChecker.git
cd PasswordChecker
```

No additional packages to install.

## Usage

```bash
python3 app.py
```

Type `q` at the prompt to exit. Enter any password to analyze its strength.

### Example

```
Welcome to Password Checker!
Type 'q' to exit

Enter a password: MyP@ssw0rd!
--------------------
  PASSWORD CHECKER
--------------------
Password: **********
Score: 5/5
Rating: ✔️ Strong ✔️

Feedback:
    ✔️ Good length (11 characters).
    ✔️ Contains uppercase letters
    ✔️ Contains lowercase letters
    ✔️ Contains numbers
    ✔️ Contains special characters
--------------------
```

## Scoring

Each passed check adds 1 point. If the password is in the common-password blacklist, the score is immediately 0.

| Score | Rating           |
|-------|------------------|
| 0–1   | Extremely Weak   |
| 2     | Very Weak        |
| 3     | Weak             |
| 4     | Poor             |
| 5     | Strong           |

## Project Structure

```
PasswordChecker/
├── app.py          # Main application
└── .gitattributes  # Git line-ending configuration
```

## Roadmap / Planned Expansion

This project is a work-in-progress. Planned improvements include:

- Larger common-password database (e.g., Have I Been Pwned API or a bundled wordlist)
- Richer scoring (weighted criteria, bonus for length > 12)
- Support for reading passwords from a file or pipe (non-interactive mode)

Contributions and suggestions are welcome.

## Notes

- Common-password blacklist includes: `password`, `admin`, `user`, `12345`, `54321`, `qwerty`
- The password is echoed in plain text during input (no masking) — use in a trusted environment
- This is a learning / demonstration project
