from prac_07.guitar import Guitar


def main():
    filename = "guitars.csv"


    guitars = load_guitars(filename)
    print("Original list of guitars:")
    display_guitars(guitars)


    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)


    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)


    guitars.sort()
    print("\nUpdated list of guitars:")
    display_guitars(guitars)


    save_guitars(filename, guitars)
    print(f"\nAll guitars saved to {filename}.")


def load_guitars(filename):
    """Read guitars information from file and return list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of Guitar objects with numbering."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Prompt user to enter new guitars and return them as a list."""
    guitars = []
    print("\nEnter new guitars (blank name to finish):")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
        except ValueError:
            print("Invalid input! Please enter a valid year and cost.")
            continue
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.\n")
        name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Save all guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
