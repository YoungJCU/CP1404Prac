from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi - initial version with manual checks."""
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 4)
    fancy_taxi.drive(0)
    print(fancy_taxi)

    fancy_taxi.drive(18)
    print(f"Fare for 18km trip: ${fancy_taxi.get_fare() + SilverServiceTaxi.flagfall:.2f}")

if __name__ == "__main__":
    main()
