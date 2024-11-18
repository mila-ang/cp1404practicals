"""
CP1404 - Practical
Taxi Test
"""

from taxi import Taxi


def main():
    # Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
    my_taxi = Taxi("Prius 1", 100, 1.23)

    # Drive taxi 40km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare)
    my_taxi.start_fare()

    # Drive the car 100 km
    my_taxi.drive(100)

    # Print the details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()
