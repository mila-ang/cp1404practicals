"""
CP1404 - Practical
Silver Service Taxi
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness  # Scale price per km
        self.fanciness = fanciness
