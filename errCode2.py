import pdb
pdb.set_trace()
user_funds = 10.31
item_price = 10.0

if item_price < user_funds:
    Print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money!")
elif item_price > user_funds:
    print("sorry you don't have enough money?")
