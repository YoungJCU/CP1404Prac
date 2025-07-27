from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar by simulating multiple drive attempts."""
    reliable_car = UnreliableCar("Reliable-ish", 100, 80)
    unreliable_car = UnreliableCar("Barely Works", 100, 30)

    print("Testing 80% reliable car over 10 attempts:")
    for i in range(10):
        distance = reliable_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance} km")

    print("\nTesting 30% reliable car over 10 attempts:")
    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance} km")

if __name__ == "__main__":
    main()