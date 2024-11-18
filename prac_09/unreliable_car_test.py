"""
CP1404 - Practical
Unreliable Car Test
"""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar Class"""
    # Create instances of UnreliableCar
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Mostly Unreliable", 100, 10)

    # Drive each car multiple times
    for i in range(10):
        distance = 10
        print(f"Attempt {i + 1}:")
        print(f"{reliable_car} drove {reliable_car.drive(distance)}km")
        print(f"{unreliable_car} drove {unreliable_car.drive(distance)}km")
        print()


main()
