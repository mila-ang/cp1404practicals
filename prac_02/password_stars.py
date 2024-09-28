"""
CP1404 - Practical
Password Stars
"""

MINIMUM_LENGTH = 8


def main():
    """Get valid password and print asterisks based on length"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password from user and check if it meets the minimum character length"""
    password = ""
    while len(password) < MINIMUM_LENGTH:
        password = input("Please enter a password: ")
        if len(password) < MINIMUM_LENGTH:
            print(f"Password must be at least {MINIMUM_LENGTH} characters long. Try again.")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of user password"""
    print('x' * len(password))


main()
