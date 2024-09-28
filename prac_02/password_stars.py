"""
CP1404 - Practical
Password Stars
"""

MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = ""
    while len(password) < MINIMUM_LENGTH:
        password = input("Please enter a password: ")
        if len(password) < MINIMUM_LENGTH:
            print(f"Password must be at least {MINIMUM_LENGTH} characters long. Try again.")
    return password


def print_asterisks(password):
    print('x' * len(password))


main()
