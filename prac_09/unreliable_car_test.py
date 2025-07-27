from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar functionality - initial version."""
    test_car = UnreliableCar("Test Unreliable", 100, 50)
    print(test_car.drive(20))  # Should print 0 for now

if __name__ == "__main__":
   main()