"""
CP1404 - Practical
Silver Service Taxi Test
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    # Create a SilverServiceTaxi instance
    hummer = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18 km
    hummer.drive(18)
    print(hummer)
    print(f"Fare for 18 km: ${hummer.get_fare():.2f}")
    assert hummer.get_fare() == 48.78, "Fare calculation is incorrect!"

    # Start a new fare and drive 50 km
    hummer.start_fare()
    hummer.drive(50)
    print(hummer)
    print(f"Fare for 50 km: ${hummer.get_fare():.2f}")


main()
