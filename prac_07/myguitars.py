from prac_07. guitar import Guitar

def main():
    filename = "guitars.csv"

    guitars=load_guitars(filename)
    print("Original list of guitars:")
    display_guitars(guitars)

    # Sort by year (oldest to newest)
    guitars.sort()

    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)


def load_guitars(filename):
    """Read guitars information and display a list"""
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
    """Display a list of guitar."""
    for guitar in guitars:
        print(guitar)


main()