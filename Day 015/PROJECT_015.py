import data

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report(current_resources):
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${current_resources['money']}")


def get_coins():
    print("Please insert coins.")
    quarters = int(input("    How many quarters? "))
    dimes = int(input("    How many dimes? "))
    nickles = int(input("    How many nickles? "))
    pennies = int(input("    How many pennies? "))
    return quarters * data.COINS["quarter"] \
           + dimes * data.COINS["dime"] \
           + nickles * data.COINS["nickle"] \
           + pennies * data.COINS["penny"]



def check_resources(current_resources, selected_coffee_type):
    if data.MENU[selected_coffee_type]["ingredients"]["water"] > current_resources["water"]:
        return False, "Sorry, there is not enough water."
    if data.MENU[selected_coffee_type]["ingredients"]["coffee"] > current_resources["coffee"]:
        return False, "Sorry, there is not enough coffee."
    if selected_coffee_type != "espresso" and data.MENU[selected_coffee_type]["ingredients"]["milk"] > current_resources["milk"]:
        return False, "Sorry, there is not enough milk."
    return True, "Enough resources."


while True:
    print("\nCoffees MENU: \n   Espresso $1.50 \n   Latte $2.50 \n   Cappuccino $3.00")
    choice = input("What would you like to have? espresso (e), latte (l) or cappuccino (c)? ")
    if choice == 'report':
        print_report(resources)
        continue
    if choice != "e" and choice != "l" and choice != "c":
        print("Not available!")
        continue
    coffee_type = "espresso" if choice == "e" else "latte" if choice == "l" else "cappuccino"
    is_enough_resources = check_resources(resources, coffee_type)
    if not is_enough_resources[0]:
        print(is_enough_resources[1])
        continue
    coins_sum = get_coins()
    if coins_sum < data.MENU[coffee_type]["cost"]:
        print("Sorry, not enough money. Money refunded.")
        continue
    else:
        resources["money"] -= data.MENU[coffee_type]["cost"]
        resources["water"] -= data.MENU[coffee_type]["ingredients"]["water"]
        resources["coffee"] -= data.MENU[coffee_type]["ingredients"]["coffee"]
        if not coffee_type == "espresso":
            resources["milk"] -= data.MENU[coffee_type]["ingredients"]["milk"]
        change = coins_sum - data.MENU[coffee_type]['cost']
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee_type}. Enjoy!")

