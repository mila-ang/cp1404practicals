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
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Choose a taxi (feature coming soon!)")
        elif choice == "d":
            print("Drive the selected taxi (feature coming soon!)")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()

    print("Goodbye!")


main()
