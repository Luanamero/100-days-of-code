from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

in_function = True

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()


while in_function:
    options = menu.get_items()
    client_choice = input(f"What would you like? ({options})")
    if client_choice == "off":
        in_function = False
    elif client_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        choosen_drink = menu.find_drink(client_choice)
        if coffe_maker.is_resource_sufficient(choosen_drink) and money_machine.make_payment(choosen_drink.cost):
            coffe_maker.make_coffee(choosen_drink)
