"""
estimate:60
actual:
"""

email=input("Email: ").strip()
name_split=email.split('@')[0]
name_clean=name_split.replace('.',' ')
names=name_clean.title()
print(names)

while email != "":
