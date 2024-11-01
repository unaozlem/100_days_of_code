from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True


while is_on:
    items = menu.get_items()
    choice = input(f"What would you like to drink? {items}: ")

    if choice == "off":
        print("Turning off the coffee machine")
        is_on = False
    elif choice == "report":
        coffee_maker.report() 
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            print("Insert coins please")
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)