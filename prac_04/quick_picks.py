import random

# Constants for the quick pick game
NUMBERS_PER_PICK = 6  # Each quick pick contains 6 numbers
MIN_NUMBER = 1        # The minimum number allowed in a quick pick
MAX_NUMBER = 45       # The maximum number allowed in a quick pick


def main():
    """Generate quick picks based on user input."""
    number_of_picks = int(input("How many quick picks? "))

    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a single quick pick with 6 unique random numbers."""
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    return quick_pick


main()
