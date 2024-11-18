"""
CP1404 - Practical
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = ("q)uit, "
        "c)hoose taxi, "
        "d)rive")


def main():
    """Simulate a taxi ride with options to choose taxis, drive, and view the bill."""
    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice not in ["c", "d"]:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()

    print("Goodbye!")


main()
