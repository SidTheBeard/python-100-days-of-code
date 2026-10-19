import random

def roshambo():
    user_choice = input("Choose your weapon: Rock(1), Paper(2), Scissors(3)")
    options = ["Rock", "Paper", "Scissors"]
    rand = int(random.random() * 3)
    
    if not check_validity(user_choice):
        return
    user_choice = int(user_choice)

    while options[user_choice-1] == options[rand]:
        print(f"You chose: {options[user_choice-1]}")
        print(f"The computer chose: {options[rand]}")
        print("Draw, play again")
        user_choice = input("Choose your weapon: Rock(1), Paper(2), Scissors(3)")
        if not check_validity(user_choice):
            return
        user_choice = int(user_choice)
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
    
def check_validity(choice):
    try:
        choice = int(choice)

        if choice != 1 and choice != 2 and choice != 3:
            print("You lose, follow instructions next time")
            return False

    except ValueError:
        print("You lose, follow instructions next time")

        return False
        
    return True


roshambo()