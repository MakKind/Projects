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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_off = False
money = 0

while not turn_off:
    action = input("What would you like? (espresso/latte/cappuccino): ")

    if action == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif action == 'off':
        turn_off = True
    elif action == "espresso" or action == "latte" or action == "cappuccino":
        if MENU[action]["ingredients"]["water"] > resources['water']:
            print("Not enough Water.")
        elif MENU[action]["ingredients"]['coffee'] > resources['coffee']:
            print("Not enough coffee.")
        elif action != "espresso" and MENU[action]["ingredients"]['milk'] > resources['milk']:
            print("Not enough Milk.")
        else:
            print("Please insert coins.")
            money_with_customer = int(input("How many quarters: ")) * 0.25 + int(
                input("How many dimes: ")) * 0.10 + int(
                input("How many nickels: ")) * 0.05 + int(input("How many pennies: ")) * 0.01
            if money_with_customer >= MENU[action]['cost']:
                print(f"Here is ${int(money_with_customer - MENU[action]['cost'])} in change.")
                print(f"Here is your {action}. Enjoy!")
                resources['water'] = resources['water'] - MENU[action]["ingredients"]["water"]
                if action != "espresso":
                    resources['milk'] = resources['milk'] - MENU[action]["ingredients"]['milk']
                resources['coffee'] = resources['coffee'] - MENU[action]["ingredients"]['coffee']
                money += MENU[action]['cost']
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Your input is wrong. Enter again.")