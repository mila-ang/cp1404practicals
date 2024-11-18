"""
CP1404 - Practical
Unreliable Car
"""

from car import Car
import random


class UnreliableCar(Car):
    """A car that may not always drive depending on its reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than its reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
