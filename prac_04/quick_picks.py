import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    how_many = int(input("How many quick picks? "))
    for _ in range(how_many):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    return numbers

main()
