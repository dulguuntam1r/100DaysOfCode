#16th day challenge
#Making day 15 project using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


print("Welcome to coffee machine")

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
game_end = False


while not game_end:
    main_menu = input("What would you like to do? ").lower()
    if main_menu == "off":
        game_end = True
    elif main_menu == "coffee":
        choice = my_menu.find_drink(input(f"What would you like to drink? {my_menu.get_items()}: ").lower())
        if my_money_machine.make_payment(choice.cost) and my_coffee_maker.is_resource_sufficient(choice):
                my_coffee_maker.make_coffee(choice)
    elif main_menu == "report":
        my_coffee_maker.report()
        my_money_machine.report()