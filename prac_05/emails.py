"""
estimate:60
actual:48
"""


email_to_name = {}

email = input("Email: ").strip()

while email != "":
    name_split = email.split('@')[0]
    name_clean = name_split.replace('.', ' ')
    name = name_clean.title()

    name_check = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if name_check not in ("", "y"):
        name = input("Name: ")

    email_to_name[email] = name

    email = input("Email: ").strip()

for email, name in email_to_name.items():
    print(f"{name} ({email})")
