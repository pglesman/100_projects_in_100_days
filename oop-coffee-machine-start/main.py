from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

while True:
    order_name = input(f"What would you like? ({menu.get_items()})")
    if order_name == "off":
        break

    if order_name == "report":
        coffee_machine.report()
        money.report()
        continue

    drink = menu.find_drink(order_name)
    if not drink:
        continue

    if coffee_machine.is_resource_sufficient(drink):
        if money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
