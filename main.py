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
    "money": 0,
}
machine_status = True


def check_resources(drink_ingredients):
    for ingr in drink_ingredients:
        if resources[ingr] < drink_ingredients[ingr]:
            print(f"Sorry there is not enough {ingr}.")
            return False
    return True


def produce_drink(drink, drink_ingredients):
    for ingr in drink_ingredients:
        resources[ingr] -= drink_ingredients[ingr]
    print(f"Here is your {drink}. Enjoy!")


def process_coins():
    """Returns the income budget calculated from coins inserted."""
    print("Please insert coins.")
    res = int(input("how many quarters?: ")) * 0.25
    res += int(input("how many dimes?: ")) * 0.1
    res += int(input("how many nickles?: ")) * 0.05
    res += int(input("how many pennies?: ")) * 0.01
    return res


def perform_transaction(budget, drink):
    """Minus resources, adds money and returns the change"""
    cost = MENU[drink]["cost"]
    if budget < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    resources['money'] += cost
    change = round(budget - cost, 2)
    if change:
        print(f"Here is ${change} dollars in change.")
    return True


while machine_status:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_status = False
    elif choice == "report":
        print(f"Water: {resources.get('water', 0)}ml")
        print(f"Milk: {resources.get('milk', 0)}ml")
        print(f"Coffee: {resources.get('coffee', 0)}g")
        print(f"Money: ${resources.get('money', 0)}")

    elif choice in MENU.keys():
        ingredients = MENU[choice]["ingredients"]
        if check_resources(ingredients):
            income = process_coins()
            if perform_transaction(income, choice):
                produce_drink(choice, ingredients)
