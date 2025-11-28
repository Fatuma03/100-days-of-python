from operator import truediv

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
}
#TODO 1: print report
#TODO 2 : check resources sufficient

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
         print(f"Sorry there is not enough {item}.")
         return False
    return True

#TODO 3: Process Coins

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters: "))* 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

#TODO 4 :check transaction successful
def is_transaction_successful(payment_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment_received < drink_cost:
        print("Sorry that's not enough money. Money Refunded.")
        return False
    else:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is your ${change} in change")
        global profit
        profit += drink_cost
        return True

#TODO 5 : Make coffee
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")



profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])




