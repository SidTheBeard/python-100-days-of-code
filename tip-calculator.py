def tip_calculator():
    total = input("What was the total of the bill?")
    tip_pct = input("What % would you like to tip?")
    ppl = int(input("How many people to split the bill?"))
    tip_pct = float(tip_pct)
    total = float(total)
    print(type(tip_pct))
    tip_pct /= 100
    total_tip = total * tip_pct
    price = total + total_tip
    print(f"Price: ${price:.2f}")
    print(f"You should tip ${total_tip:.2f}")
    print(f"Each of the {ppl} people owes ${(price / ppl):.2f}")
    return total_tip
    
tip_calculator()