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
    assert hummer.get_fare() == 48.80, "Fare calculation is incorrect!"

    # Start a new fare and drive 35 km
    hummer.start_fare()
    hummer.drive(35)
    print(hummer)
    assert hummer.get_fare() == round(35 * 2.46 + 4.50, 1), "Fare rounding logic failed!"

    # Start another fare and drive 1 km
    hummer.start_fare()
    hummer.drive(1)
    print(hummer)
    assert hummer.get_fare() == 6.96, "Small fare calculation failed!"


main()
