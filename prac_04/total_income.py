"""
CP1404/CP5632 Practical
Starter code for cumulative total income program

"""


def main():
    """Display income report for incomes over a given number of month_number."""
    incomes = []
    month_number = int(input("How many month? "))


    for month in range(1, month_number + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    display_income_report(month_number, incomes)

def display_income_report(month_number,incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_number + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()