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
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                total_bill += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive.")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Display available taxis and let the user choose one."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the trip cost."""
    try:
        distance = float(input("Drive how far? "))
        taxi.start_fare()
        taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid input")
        return 0.0


main()
