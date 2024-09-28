"""
CP1404 - Practical
Password Stars
"""

minimum_length = 8
password = ""
while len(password) < minimum_length:
    password = input("Please enter a password: ")
    if len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long. Try again.")

print('x' * len(password))
