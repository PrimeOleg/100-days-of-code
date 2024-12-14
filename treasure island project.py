print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# first choice - crossroads
crossroads_choice = input("You are at the crossroads "
                          "where do you want to go: "
                          "\"left\" or \"right\":\n")
if crossroads_choice == "left".lower():
    # second choice - lake wait/swim
    lake_choice = input("You are now in front of the lake "
                        "what do you want to do: "
                        "\"swim\" or \"wait\":\n")
    if lake_choice == "wait".lower():
        # third choice - 3 doors - red, blue, yellow
        door_choice = input("Suddenly 3 doors are in front of you "
                            "which one do you open: "
                            "\"red\", or \"blue\" or \"yellow\":\n")
        if door_choice == "red".lower():
            print("You open the door and the flame burns you;"
                  "\nYOU DIE!")
        elif door_choice == "blue".lower():
            print('The door opens and a wave of sword flies at you'
                  '\nYOU DIE!')
        elif door_choice == "yellow".lower():
            print("You get showered with riches;"
                  "\nYOU WIN!")
        else:
            print("You hesitate and trip over a rock hitting your head"
                  "\nYOU DIE!")
    else:
        print("The boat breaks in the middle of the ocean and you get eaten by sharks"
              "\nYOU DIE!")
else:
    print("You got killed by the bandits"
          "\nYOU DIE!")
