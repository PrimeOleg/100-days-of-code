import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def winning_conditions(user_cards, computer_cards):
    if sum(computer_cards) == 21:
        return "Computer wins! with a Blackjack!"
    elif sum(user_cards) == 21:
        return "User wins! with a Blackjack!"
    elif sum(computer_cards) == 21 and sum(user_cards) == 21:
        return "Draw!"
    elif sum(user_cards) > 21:
        return "Computer wins! User went over 21!"
    elif sum(computer_cards) > 21:
        return "User wins! Computer went over 21!"
    elif sum(computer_cards) > sum(user_cards):
        return "Computer wins!"
    else:
        return "User wins!"

# Dealing cards
def main():
    game = True
    while game:
        print(logo)
        replay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if replay == 'n':
            game = False
            print("Thank you for playing!")

        elif replay == 'y':
            print("\n" * 20)
            user_cards = []
            for i in range(0, 2):
                if i == 11:
                    if sum(user_cards) + i > 21:
                        user_cards.append(1)
                else:
                    user_cards.append(random.choice(cards))
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")

            computer_cards = []
            for i in range(0, 2):
                if i == 11:
                    if sum(computer_cards) + i > 21:
                        computer_cards.append(1)
                else:
                    computer_cards.append(random.choice(cards))
            print(f"Computer's first card: {computer_cards[0]}")

            draw = input("Type 'y' to get another card, type 'n' to pass: ")

            if draw == 'y':
                user_cards.append(random.choice(cards))
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
                if sum(user_cards) > 21:
                    game = False
                    print(winning_conditions(user_cards, computer_cards))
            elif draw == 'n':
                while sum(computer_cards) < 16:
                    computer_cards.append(random.choice(cards))
                print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
                print(winning_conditions(user_cards, computer_cards))

main()
