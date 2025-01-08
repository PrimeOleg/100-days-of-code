import resource

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def enough_resources(ingredients):
    """Function returning True or False by checking if there are enough resources to make coffee"""
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}')
            return False
        return True

def process_money():
    """Function for calculation of total coins user entered excluding change"""
    print('Insert Coins.')
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    return total_coins

def success_transaction(total_coins, drink_cost):
    """Function calculating if the user has inputted enough money and adding it to the total amount"""
    if total_coins < drink_cost:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
    elif total_coins >= drink_cost:
        global money
        money += drink_cost
        print(f'Here is ${round(total_coins - drink_cost, 2)} dollars in change.')
        return True

def make_coffee(drink_name, ingredients):
    """Function that will output and deduct the coffee ingredients"""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f'Here is your {drink_name} ☕️')


machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
    elif user_choice == 'off':
        machine_on = False
    else:
        drink = MENU[user_choice]
        if enough_resources(drink['ingredients']):
            payment = process_money()
            success_transaction(payment, drink['cost'])
            make_coffee(user_choice, drink['ingredients'])
