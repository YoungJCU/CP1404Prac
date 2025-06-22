"""
estimate: 60
actual:
"""
FILENAME = "wimbledon.csv"
def main():
    data = read_wimbledon_data(FILENAME)

def read_wimbledon_data(FILENAME):
    """Read the CSV file and return a list."""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            data.append([champion, country])
    return data

main()