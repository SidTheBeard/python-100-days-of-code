from art import *
import higher_lower_game_data as gd
import random

titleArt = """
█  █ ▀█▀ ▄▀▀▀ █  █ █▀▀▀ █▀▀▄ 
█▀▀█  █  █ ▀█ █▀▀█ █▀▀  █▀█  
▀  ▀ ▀▀▀  ▀▀▀ ▀  ▀ ▀▀▀▀ ▀  ▀ 
                             
█    ▄▀▀▄ █   █ █▀▀▀ █▀▀▄    
█    █  █ █▄▀▄█ █▀▀  █▀█     
▀▀▀▀  ▀▀  ▀   ▀ ▀▀▀▀ ▀  ▀    
"""
vs = """
█   █ ▄▀▀▀ 
▀▄ ▄▀  ▀▀▄ 
  ▀   ▀▀▀  
"""

streaking = True
incumbent = None
score = 0

print(titleArt)
while streaking:
    if incumbent == None:
        incumbent = random.choice(gd.data)
    
    option2 = random.choice(gd.data)
    while option2["name"] == incumbent["name"]:
        option2 = random.choice(gd.data)

    answer = incumbent["name"] if incumbent["follower_count"] > option2["follower_count"] else option2["name"]
    print(f"Score: {tprint(f"Score:   {score}")}")
    print(f"Compare A: {incumbent["name"]}, a{"n" if incumbent["description"][0].lower() in ["a","e","i","o","u"] else ""} {incumbent["description"]} from {incumbent["country"]}")
    print(incumbent)
    print(vs)
    print(f"Against B: {option2["name"]}, a{"n" if option2["description"][0].lower() in ["a","e","i","o","u"] else ""} {option2["description"]} from {option2["country"]}")
    print(option2)
    choice = input("Which has a larger following? Enter 'A' or 'B':")
    while choice.lower() != 'a' and choice.lower()!= 'b':
        print("Invalid entry")
        choice = input("Which has a larger following? Enter 'A' or 'B':")
        
    if choice.lower() == "a":
        if incumbent["follower_count"] > option2["follower_count"]:
            streaking = True
            score += 1
        else:
            streaking = False
    elif choice.lower() == "b":
        if incumbent["follower_count"] > option2["follower_count"]:
            streaking = False
        else:
            incumbent = option2
            score += 1

tprint("You   Lose!")
tprint(f"Final   Score:   {score}")
