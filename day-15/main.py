# Coffee Machine Project
import sys

def off():
    print("Powering Off...")
    sys.exit()

serving = True
resources = {
    "coffee": 100, # in grams
    "milk": 200, # 4 gallons in mL
    "money": 0, # cash in register
    "water": 300, # 4 gallons in mL
}
recipes = {
    "cappuccino": {
        "coffee": 50,
        "cost": 3,
        "milk": 150,
        "water": 250,
    },
    "espresso": {
        "coffee": 18,
        "cost": 1.5,
        "milk": 0,
        "water": 50,
    },
    "latte": {
        "coffee": 24,
        "cost": 2.5,
        "milk": 150,
        "water": 200,
    },
}

while serving is True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    prepped = choice.lower()
    if prepped == "off":
        off()
    
    if prepped == "report":
        print("\n")
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {resources["money"]:.2f}")
        print("\n")
        
    
    if prepped in recipes:
        print(recipes[prepped])
        not_enough_coffee = resources["coffee"] < recipes[prepped]["coffee"]
        not_enough_milk = resources["milk"] < recipes[prepped]["milk"]
        not_enough_water = resources["water"] < recipes[prepped]["water"]
        if not_enough_coffee:
            print("Sorry, there is not enough coffee for that")
        elif not_enough_milk:
            print("Sorry, there is not enough milk for that")
        elif not_enough_water:
            print("Sorry, there is not enough water for that")
        else:
            print(f"That'll be ${recipes[prepped]["cost"]:.2f}")
            print("Please insert coins.")
            quarters = ""
            dimes = ""
            nickels = ""
            pennies = ""
            
            while not quarters.isdigit():
                quarters = input("How many quarters?: ")
            while not dimes.isdigit():
                dimes = input("How many dimes?: ")
            while not nickels.isdigit():
                nickels = input("How many nickels?: ")
            while not pennies.isdigit():
                pennies = input("How many pennies?: ")
            
            quarters = int(quarters) * 0.25
            dimes = int(dimes) * 0.1
            nickels = int(nickels) * 0.05
            pennies = int(pennies) * 0.01
            
            received = quarters + dimes + nickels + pennies

            if received >= recipes[prepped]["cost"]:
                print(f"{prepped.title()} coming right up!")
                resources["money"] += recipes[prepped]["cost"]
                diff = float(received) - float(recipes[prepped]["cost"])
                if diff > 0:
                    print(f"Here's your change: ${diff:.2f}")
                    
                resources["coffee"] -= recipes[prepped]["coffee"]
                resources["milk"] -= recipes[prepped]["milk"]
                resources["water"] -= recipes[prepped]["water"]
            else:
                print(f"Sorry that's not enough for a{"n" if prepped == "espresso" else ""} {prepped}, money refunded")
