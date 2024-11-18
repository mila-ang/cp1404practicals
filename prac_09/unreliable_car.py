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

