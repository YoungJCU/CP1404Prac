from prac_06.guitars import Guitar
gibson=Guitar("Gibson L-5 CES",1922,"16,035.40")

print(gibson)
print(gibson.get_age())

another = Guitar("Another Guitar", 2013, 1200.00)

expected_gibson_age = 2025 - 1922

actual_gibson_age = gibson.get_age()
print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {actual_gibson_age}")

expected_another_age = 2025 - 2013

actual_another_age = another.get_age()
print(f"{another.name} get_age() - Expected {expected_another_age}. Got {actual_another_age}")


expected_gibson_vintage = True
actual_gibson_vintage = gibson.is_vintage()
print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {actual_gibson_vintage}")

expected_another_vintage = False
actual_another_vintage = another.is_vintage()
print(f"{another.name} is_vintage() - Expected {expected_another_vintage}. Got {actual_another_vintage}")
