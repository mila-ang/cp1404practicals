"""
CP1404 - Practical
Unreliable Car Test
"""

from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar Class"""
    # Create instances of UnreliableCar
    cars = [UnreliableCar("Always Reliable", 100, 100),
        UnreliableCar("Never Reliable", 100, 0),
        UnreliableCar("Mostly Reliable", 100, 90),
        UnreliableCar("Mostly Unreliable", 100, 10)]

    # Test each car
    for car in cars:
        print(f"Testing {car.name}")
        for i in range(5):
            distance = 5
            print(f"Attempt {i + 1}: {car.name} drove {car.drive(distance)}")
            print()


main()
