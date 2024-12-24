from art import logo, game_over_logo, victory
import random

NUMBER = random.randint(1, 100)
EASY_LEVEL = 10
HARD_LEVEL = 5

def game(difficulty):
    """Main game function that takes user's input of difficulty when the function is called."""
    if difficulty.lower() == "easy":
        attempts = EASY_LEVEL
    else:
        attempts = HARD_LEVEL

    # loop will run as long as user has attempts remaining
    game_over = False
    while not game_over:
        print(NUMBER)
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == NUMBER or attempts < 1:
            game_over = True
        elif guess < NUMBER:
            print("Your guess is too low.")
            attempts -= 1
        elif guess > NUMBER:
            print("Your guess is too high.")
            attempts -= 1


    if guess == NUMBER:
        print(f"Congratulations, you guessed the number {NUMBER}.")
        print(victory)
    else:
        print(f"Sorry, you didn't guess the number. The number was {NUMBER}")
        print(game_over_logo)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game(input("Choose a difficulty type 'easy' or 'hard': "))

