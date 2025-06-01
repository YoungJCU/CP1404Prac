def main():
    password=get_password()
    print_symbol(password,"*")




def get_password():
    """Get valid password"""
    password=input("Enter password: ")
    while len(password) <= 6:
        print("Invalid")
        password = input("Enter password: ")
    return password

def print_symbol(password, symbol):
    print(symbol * len(password))



main()