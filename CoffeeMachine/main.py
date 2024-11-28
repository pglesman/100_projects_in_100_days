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
    "money": 0
}

coins_inserted = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}

services = ['report', 'off']


def counting_coins(coins: dict) -> float:
    """Return the sum of the coins."""
    coins_sum = 0
    for key, value in coins.items():
        if key == "quarters":
            coins_sum += value * 0.25
        elif key == "dimes":
            coins_sum += value * 0.10
        elif key == "nickles":
            coins_sum += value * 0.05
        elif key == "pennies":
            coins_sum += value * 0.01
    return coins_sum


def resources_report(supplies: dict) -> None:
    """Report remaining supplies from a dictionary."""
    for keys, values in supplies.items():
        if keys in ["water", "milk"]:
            value = f"{values}ml"
        elif keys == "coffee":
            value = f"{values}g"
        else:
            value = f"${values}"
        print(f"{keys.title()}: {value}")


def resources_deduction(coffee: str, supplies: dict) -> None:
    """Deduct resources from the supplies depend on which coffee has been chosen."""
    coffee_resources = MENU[coffee]["ingredients"]
    for key in supplies.keys():
        if key == 'milk' and coffee == 'espresso':
            continue
        supplies[key] -= coffee_resources[key]
        if key == "coffee":
            break
    supplies["money"] += MENU[coffee]["cost"]


while True:
    sufficiency = True

    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice not in MENU.keys() and coffee_choice not in services:
        print("I don't understand the answer. Please write again.")
        continue

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee_choice == services[1]:
        print("Coffee Machine will be shut down. Goodbye.")
        break

    # TODO 3: Print report.
    if coffee_choice == services[0]:
        resources_report(resources)
        continue

    # TODO 4: Check resources sufficient?
    coffee_ingredients = MENU[coffee_choice]["ingredients"]
    for k, v in coffee_ingredients.items():
        if v > resources[k]:
            print(f"Sorry, there is not enough {k}.")
            sufficiency = False
            break

    if not sufficiency:
        continue

    # TODO 5: Process coins.
    print("Please insert coins.")
    for k in coins_inserted.keys():
        coins_inserted[k] = int(input(f"How many {k}?: "))

    # TODO 6: Check transaction successful?
    money_diff = counting_coins(coins_inserted) - MENU[coffee_choice]["cost"]
    if money_diff < 0:
        print(f"Sorry that's not enough money. Money refunded. You need ${abs(money_diff):.2f} more.")
        continue

    if money_diff:
        print(f"Here is ${money_diff:.2f} in change.")

    # TODO 7: Make Coffee.
    print(f"Here is your {coffee_choice} ☕ Enjoy!")
    resources_deduction(coffee_choice, resources)
    resources_report(resources)
