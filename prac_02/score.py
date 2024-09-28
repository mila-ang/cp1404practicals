"""
CP1404 - Practical
Program to determine score status
"""

import random


def main():
    # Get user input and result
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    # Get random score and result
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")


def determine_result(score):
    """Return the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
