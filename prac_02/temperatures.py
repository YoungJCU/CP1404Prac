"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit=transform_celsius_to_fahrenheit()
            print(celsius_to_fahrenheit)
        elif choice == "F":
            fahrenheit_to_celsius=transform_fahrenheit_to_celsius()
            print(fahrenheit_to_celsius)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def transform_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"

def transform_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"Result: {celsius:.2f} C"

main()