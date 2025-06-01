
MENU="(G)et score (P)rint score (S)how stars (Q)uit"

def main():
    print(MENU)
    choice=get_choice()

    while choice != "Q":
        if choice == "G":
            score=get_valid_score()
            print(MENU)
            choice = get_choice()

        elif choice =="P":
            print(determine_score_category(score))
            print(MENU)
            choice = get_choice()

        elif choice =="S":
            print_symbol(score,"*")
            print(MENU)
            choice = get_choice()
        else:
            print("Invalid")
            print(MENU)
            choice = get_choice()

    print("Farewell")

def get_valid_score():
     score=int(input("Enter score: "))
     while score <0 or score > 100:
         print("Invalid")
         score = int(input("Enter score: "))
     return score

def get_choice():
    choice=input("Enter choice: ").upper()
    return choice

def determine_score_category(score):
    if score > 90:
        message="Excellent"
    if score > 50:
        message="Passable"
    else:
        message="Bad"
    return message

def print_symbol(score, symbol):
    print(symbol * score)
main()