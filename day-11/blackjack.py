import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def show_hand(hand):
    for card in hand:
        print(ascii_card(card))
def calculate_score(hand):
    if sum(hand) == 21:
        return 0
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
def deal_card():
    toReturn = random.choice(cards)
    cards.pop(cards.index(toReturn))
    return toReturn
def ascii_card(rank):
    formatted = rank if len(str(rank)) == 2 else f" {rank}"
    template = """
┌─────────┐
│{}       │
│         │
│         │
│         │
│       {}│
└─────────┘
""".format(formatted, formatted)
    return template

print(logo)
dealer = []
user = []
dealer_first = deal_card()
user_first = deal_card()
dealer.append(dealer_first)
user.append(user_first)
dealing_dealer = True
dealing_user = True
while dealing_user and len(cards) > 0:
    user_score = calculate_score(user)
    if(user_score > 0 and user_score < 21):
        print("Dealer hand:\n")
        show_hand(dealer)
        print("User hand:\n")
        show_hand(user)
        print(f"User's Turn, currently at {sum(user)}")
        should_continue = input("Hit?\n").lower()
        if should_continue != "hit" and should_continue != "yes":
            dealing_user = False
        else:
            new_card = deal_card()
            user.append(new_card)
            print(ascii_card(new_card))
    else:
        if user_score != 0:
            print(f"You bust with {user_score}!\n")
            show_hand(user)
        dealing_user = False
        dealing_dealer = False

while dealing_dealer and len(cards) > 0:
    dealer_score = calculate_score(dealer)
    if(dealer_score > 0 and dealer_score < 21):
        print("Dealer hand:\n")
        show_hand(dealer)
        print(f"Dealer's Turn, currently at {sum(dealer)}")
        should_continue = input("Hit?\n").lower()
        if should_continue != "hit" and should_continue != "yes":
            dealing_dealer = False
        else:
            new_card = deal_card()
            dealer.append(new_card)
            print(ascii_card(new_card))
    else:
        print(f"Dealer bust with {sum(dealer)}, you win!\n")
        show_hand(user)
        dealing_dealer = False

if calculate_score(user) == 0:
    print("You have blackjack, you win!")
elif calculate_score(dealer) == 0:
    print("Dealer has blackjack, you lose!")    
elif (sum(user) > sum(dealer) and sum(user) <= 21) or sum(dealer) > 21:
    print(f"User wins! Beat the dealer {sum(user)} to {sum(dealer)}")
elif sum(user) == sum(dealer):
    print("Draw!")
else:
    print("Dealer wins!")
