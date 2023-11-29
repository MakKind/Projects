from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
turn_off = False

while not turn_off:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "report":
        coffee_maker.report()
        money.report()
    elif choice == "off":
        turn_off = True
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
