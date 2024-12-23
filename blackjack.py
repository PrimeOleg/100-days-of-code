import random
from art import logo
user = []
computer = [] 
# is_game_over Boolean can be used, based on this condition a check can be done to see if score = 0
# save the user's score as variables
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

for i in range(2):
    user.append(deal_card())
    computer.append(deal_card())

# score calculation
def calculate_score(list_of_cards):
    score = sum(list_of_cards)

    if list_of_cards[0] + list_of_cards[1] == 21: # redo a better way exists, Hint use len() and sum()
        return 0
    else:
        for card in list_of_cards: # no need for a loop as mentioned before sum() and keyword in should work and checking the score should be done outside of this function
            if card == 11:
                if score > 21:
                    list_of_cards.remove(11)
                    list_of_cards.append(1)
                    return score
        else:
            return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins! with a blackjack"
    elif user_score == 0:
        return "You win!"
    elif user_score > 21:
        return "You went over! You lose!"
    elif computer_score > 21:
        return "Computer went over! You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "Computer wins!"

def game():
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print(logo)
    draw = True
    while draw:
        if calculate_score(user) == 0 or calculate_score(computer) == 0:
            draw = False
            compare(calculate_score(user), calculate_score(computer))
        else:
            print(f"\tYour cards: {user}, current score: {calculate_score(user)}")
            print(f"\tComputer's first card: {computer[0]}")

            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == 'y':
                user.append(deal_card())
                if calculate_score(user) > 21:
                    print(f"\tYour final hand: {user}, final score: {calculate_score(user)}")
                    print(f"\tComputer's final hand: {computer}, final score: {calculate_score(computer)}")
                    print(compare(calculate_score(user), calculate_score(computer)))
                    draw = False
            else:
                draw = False
                while calculate_score(computer) < 17: # another condition is needed
                    computer.append(deal_card())
                print(f"\tYour final hand: {user}, final score: {calculate_score(user)}")
                print(f"\tComputer's final hand: {computer}, final score: {calculate_score(computer)}")
                print(compare(calculate_score(user), calculate_score(computer)))
# ALOT OF REDUNDANT LINES OF CODE WHICH CAN BE SIMPLIFIED AND BROKEN DOWN
# can be changed as while input() instead of redundant lines
    if play_again == 'y':
        print("\n" * 20)
        user.clear()
        computer.clear()
        for i in range(2):
            computer.append(deal_card())
            user.append(deal_card())
        game()
game()
