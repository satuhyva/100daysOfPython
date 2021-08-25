from coffee_maker  import CoffeeMaker
from money_machine  import MoneyMachine
from menu import MenuItem, Menu


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    print("\nCoffees MENU: \n   Espresso $1.50 \n   Latte $2.50 \n   Cappuccino $3.00")
    choice = input("What would you like to have? espresso (e), latte (l) or cappuccino (c)? ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    if choice != "e" and choice != "l" and choice != "c":
        print("Not available!")
        continue
    coffee_type = "espresso" if choice == "e" else "latte" if choice == "l" else "cappuccino"
    drink = menu.find_drink(coffee_type)
    is_enough_resources = coffee_maker.is_resource_sufficient(drink)
    if not is_enough_resources:
        continue
    paymentIsSuccessful = money_machine.make_payment(drink.cost)
    coffee_maker.make_coffee(drink)
