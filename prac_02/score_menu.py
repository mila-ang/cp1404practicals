"""
CP1404 - Practical
Score Menu
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score()

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            # Get a valid score
            score = get_valid_score()
        elif choice == "P":
            # Print result based on the score
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            # Show stars based on the score
            print_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    """Get a valid score between 0 and 100"""
    score = float(input("Enter a score between 0 and 100: "))
    while score < 0 or score > 100:
        print("Invalid score! Score must be between 0 and 100.")
        score = float(input("Enter a score between 0 and 100: "))
    return score


def determine_result(score):
    """Return result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars based on score"""
    print("x" * int(score))


main()
