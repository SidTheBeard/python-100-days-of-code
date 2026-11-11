def silent_auction():
    bidders = {}
    bidders_remaining = True
    while bidders_remaining:
        name = input("What is your name?")
        bid = float(input("What is your bid?"))
        bidders[name] = bid
        should_continue = input("Are there any bidders remaining? Type 'yes' or 'no'\n").lower()
        if should_continue == "no":
            bidders_remaining = False
            winner = ""
            highest = 0
            for bidder in bidders:
                if bidders[bidder] > highest:
                    highest = bidders[bidder]
                    winner = bidder
            print(f"The winner is: {winner}!")
        elif should_continue == "yes":
            print("\n" * 100)

silent_auction()