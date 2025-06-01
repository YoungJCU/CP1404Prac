"""
CP1404 Menus
"""
MENU="(H)ello\n(G)oodbye\n(Q)uit"

name=input("Enter name: ")
print(MENU)
choice=input(">>>").upper()

while choice != "Q":
    if choice=="H":
        print("Hello", name)
        print(MENU)
        choice = input(">>>").upper()

    elif choice=="G":
        print("Goodbye", name)
        print(MENU)
        choice = input(">>>").upper()

    else:
        print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()

print("Finished")
