import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
computer_choice = random.randint(0, 2)
# Output the choices
if player_choice < 3 and player_choice >= 0:
    print(f"You chose:\n{options[player_choice]}")
    print(f"Computer chose:\n{options[computer_choice]}")
    # In the long term separate elif statements and player_choice > computer_choice would be better
    if (player_choice == 0 and computer_choice == 2 or
        player_choice == 1 and computer_choice == 0 or
        player_choice == 2 and computer_choice == 1):
        print("You win!")
    elif player_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")
else:
    print("Invalid option entered!")
