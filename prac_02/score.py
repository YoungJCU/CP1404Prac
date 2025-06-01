"""
Cp1404 Broken score
"""

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# : Fix this!
def main():
    score=validate_score()
    score_category=determine_score_category(score)
    print(score_category)

def validate_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid")
        score = float(input("Enter score: "))
    return score


def determine_score_category(score):
    if score > 90:
        message="Excellent"
    if score > 50:
        message="Passable"
    else:
        message="Bad"
    return message

main()