from art import logo
print(logo)
# function for identifying the highest bidder
def find_highest_bidder(bid_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

replay = False
bids = {}

while not replay:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    other_bidders = input("Are there any other bidders? Types 'yes' or 'no'.\n")
    if other_bidders == 'yes':
        print("\n" * 20)

    elif other_bidders == 'no':
        find_highest_bidder(bids)
