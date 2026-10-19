import random

def roshambo():
    user_choice = int(input("Choose your weapon: Rock(1), Paper(2), Scissors(3)"))
    options = ["Rock", "Paper", "Scissors"]
    rand = int(random.random() * 3)
    
    if user_choice != 1 and user_choice != 2 and user_choice != 3:
        print("You lose, follow instructions next time")
        return
    while options[user_choice-1] == options[rand]:
        print(f"You chose: {options[user_choice-1]}")
        print(f"The computer chose: {options[rand]}")
        print("Draw, play again")
        user_choice = int(input("Choose your weapon: Rock(1), Paper(2), Scissors(3)"))
        rand = int(random.random() * 3)
        
    print(f"You chose: {options[user_choice-1]}")
    print(f"The computer chose: {options[rand]}")
    if options[user_choice-1] == "Paper":
        if options[rand] == "Scissors":
            print("You lose!")
        elif options[rand] == "Rock":
            print("You win!")
    elif options[user_choice-1]  == "Scissors":
        if options[rand] == "Rock":
            print("You lose!")
        elif options[rand] == "Paper":
            print("You win!")
    elif options[user_choice-1]  == "Rock":
        if options[rand] == "Paper":
            print("You lose!")
        elif options[rand] == "Scissors":
            print("You win!")
    return options[int(rand)]

roshambo()