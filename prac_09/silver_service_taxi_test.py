from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi fare calculation with assertions."""
    # Create a fancy taxi with fanciness of 2.0
    fancy_taxi = SilverServiceTaxi("TestFancy", 100, 2)
    fancy_taxi.drive(18)  # Drive 18 km
    expected_fare = (1.23 * 2 * 18) + 4.50  # 44.28 + 4.50 = 48.78
    actual_fare = fancy_taxi.get_fare()
    print(f"Expected fare: ${expected_fare:.2f}, Actual fare: ${actual_fare:.2f}")
    assert abs(actual_fare - expected_fare) < 0.01, "Fare calculation failed"

    # Optional: test string format
    print(fancy_taxi)
    assert "plus flagfall of $4.50" in str(fancy_taxi)

if __name__ == "__main__":
    main()

