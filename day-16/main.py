from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

available = Menu()
maker = CoffeeMaker()
register = MoneyMachine()

serving = True

maker.report()
register.report()

while serving:
    choice = input(f"What would you like? ({available.get_items()})")
    choice = choice.lower()
    if choice == "report":
        maker.report()
        register.report()
    elif choice == "off":
        serving = False
    else:
        order = available.find_drink(choice)
        if order and maker.is_resource_sufficient(order):
            if register.make_payment(order.cost):
                maker.make_coffee(order)
