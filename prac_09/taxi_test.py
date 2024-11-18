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

