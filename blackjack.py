import random
from art import logo

def deal_card():
    """Dealing a random card out of the deck to the user"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the score based on the list of cards provided"""
    if sum(cards) == 21:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Function taking the scores as inputs and comparing them to find a winning condition"""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Computer wins! with a blackjack"
    elif u_score == 0:
        return "You win!"
    elif u_score > 21:
        return "You went over! You lose!"
    elif c_score > 21:
        return "Computer went over! You win!"
    elif u_score > c_score:
        return "You win"
    else:
        return "Computer wins!"

def game():
    """Main game loop that will launch everytime the condition of the replay will be met"""
    user = []
    computer = []
    computer_score = -1
    user_score = -1
    game_over = False

    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_draw == "y":
                user.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    print(logo)
    game()
