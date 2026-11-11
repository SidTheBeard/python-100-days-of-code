def treasure_island():
    print("Welcome to Treasure Island.\nYour mission is to find the treasure")
    left_or_right = input("Left(L) or Right(R)")
    if left_or_right == "R" or left_or_right.lower() == "r":
        print("Game Over.")
        return
    swim_or_wait = input("Swim(S) or Wait(W)")
    if swim_or_wait == "S" or swim_or_wait.lower() == "s":
        print("Game Over.")
        return
    door_choice = input("Which door, Red(R), Yellow(Y) or Blue(B)")
    if door_choice != "Y" and door_choice.lower() != "y":
        print("Game Over.")
        return
    
    print("You Win!")
    return
    
treasure_island()