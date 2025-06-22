"""
estimate: 60
actual:48
"""
FILENAME = "wimbledon.csv"

def main():
    """Main function to read, process, and display Wimbledon data."""
    data = read_file(FILENAME)
    champion_counts = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for name, count in sorted(champion_counts.items()):
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_file(filename):
    """Read the CSV file and return a list of [champion, country] pairs."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 3 or not parts[2]:
                continue
            country = parts[1]
            champion = parts[2]
            records.append([champion, country])
    return records


def count_champions(data):
    """Return a dictionary mapping each champion to their win count."""
    counts = {}
    for name, _ in data:
        counts[name] = counts.get(name, 0) + 1
    return counts


def get_countries(data):
    """Return a sorted list of unique countries."""
    return sorted({country for _, country in data})


main()