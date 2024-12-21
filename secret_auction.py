from art import logo
print(logo)

name = input("What is your name?: ")
price = int(input("What is your bid?: $"))
bids = {name:price}

# function for locating the person with the highest bid
# goes through each value in the dictionary and compares them to each other assigning
# the highest bid and person's name to variables outside the for loop
def highest_bidder(bids_dictionary):
    highest_name = ""
    highest_bidder_price = 0

    for bidder in bids_dictionary:
        if bids_dictionary[bidder] > highest_bidder_price: # if 100 > 0
            highest_bidder_price = bids_dictionary[bidder] # highest_bidder_price = 100
            highest_name = bidder # highest_name = jake
    print(f"The winner is {highest_name} with a bid of ${highest_bidder_price}" )

replay = False
while not replay:
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if yes_or_no == 'yes':
        print("\n" * 20)
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price

    elif yes_or_no == 'no':
        replay = True
        highest_bidder(bids_dictionary=bids)
