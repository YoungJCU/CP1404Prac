from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi for 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    my_taxi.start_fare()

    # Drive the taxi for 100 km
    my_taxi.drive(100)

    # Print the taxi's updated details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()