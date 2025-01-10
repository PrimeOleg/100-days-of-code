import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(CARDS)

def calculate_score(deck_cards):
        for card in deck_cards:
            if 11 in deck_cards:
                if sum(deck_cards) > 21:
                    deck_cards.remove(11)
                    deck_cards.append(1)
                elif card + 11 == 21:
                    return 0
            return sum(deck_cards)
        
# TODO - The user and computer should get 2 cards each
user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

# TODO - Add the user and computer's scores
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

# TODO - Ask user if they want to draw another card
game_over = False
while not game_over:
    print(f"Your cards are: {user_cards}, current score: {user_score}")
    print(f"Computer first card is: {computer_cards[0]}")
    answer = input("Would you like to draw another card, type 'n' to pass or 'y' to draw: ")

    if answer == 'y':
        user_cards.append(deal_card())
        print(user_cards, user_score)
    else:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    # TODO - Check for winning conditions either function or within the loop













