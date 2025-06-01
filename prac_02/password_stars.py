def main():
    password=get_password()
    print("*"*len(password))




def get_password():
    """Get valid password"""
    password=input("Enter password: ")
    while len(password) <= 6:
        print("Invalid")
        password = input("Enter password: ")
    return password



main()