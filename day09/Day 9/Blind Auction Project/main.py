# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)


def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        amount = bidding_dictionary[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
bidding = True
blind_project ={}
while bidding:
    name= input("Whats your name?: ")
    price = int(input("Whats your bid?: $"))
    blind_project[name]= price
    other_users = input("Are there any bidders? Type 'yes or no': \n").lower()

    if other_users == "no":
        bidding = False
        find_highest_bidder(blind_project)
    elif other_users == "yes":
        print("\n" * 20)






