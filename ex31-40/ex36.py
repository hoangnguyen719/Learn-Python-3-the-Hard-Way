# This is a game called "Morgan 412": a guide to
# Hoang Nguyen's room in his senior year

def bathroom():
    print("This is the bath room.")
    used = input("Is door closed? ").lower()

    while used not in ["yes", "no", "nah", "yeah"]:
        used = input("Wrong answer. Is it open or not? ")

    if used in ["yeah", "yes"]:
        print("It means someone's inside. You cannot go in!")
    else:
        print("What you want to do?")
        print("1. Wash your face.")
        print("2. Take a shit.")
        action = input("> ")
        if action == "2":
            print("May I say... shit is done?!...")
            game_over('\n')
        elif action == "1":
            game_over("Your face is full of pimples!")
        else:
            game_over("Learn to type a number!")

def table():
    print("This is the table.")
    print('''What you want to do?
    1. Study
    2. Play Dota
    ''')
    action = input("> ")
    while action not in ["1", "2"]:
        print("Do you even read bro?")
        action = input("Choose again please. ")

    if action == "1":
        print("You fucking nerd?!")
    else:
        print("You fucking lazy bastard!")
        game_over("You later become unemployed and nobody loves you.")


def bed():
    print("This is the bed. Hoang sleeps here.")
    print("Are you going to sleep?")

    action = input("> ").lower()
    while action not in ["yes", "yeah", "no", "nah"]:
        action = input("I'm done with your stupidity. Choose again! ")

    if action in ["yeah", "yes"]:
        print("You took a 3-hour nap and forgot to call My.")
        game_over("You are dead meat with My.")
    else:
        print("Yes, better go back to study.")

def game_over(x):
    print(x, 'See-ya!')

def main():
    print("This is Hoang's room.")
    print('''There is a table on the left
    a bed on the right
    and a bathroom if you go straight ahead.

    Where will you go? (left/right/ahead)
    ''')
    action = input("> ").lower()

    s1 = "And you claim to be a data analyst when you can't even read?"
    s2 = "Second time already. Are you going to be serious?"
    s3 = "Seriously, last chance."
    statements = [s1, s2, s3]
    i = 0
    while (i < 3) and (action not in ["left", "right", "ahead", "quit"]):
        print(statements[i])
        action = input("TRY AGAIN! ").lower()
        i += 1

    if (action == "quit") | (i == 3):
        game_over("Alright I'm done with you.")
    else:
        if action == "left":
            table()
        if action == "right":
            bed()
        if action == "ahead":
            bathroom()

main()
