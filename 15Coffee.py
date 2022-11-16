#15th day challenge

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

money = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}

user_money = 0.0
game_end = False
print("Welcome to coffee machine")

def report():
    measurement = "ml"
    for items in resources:
        if items == "coffee":
            measurement = "g"
        print(f"{items.capitalize()}: {resources[items]}{measurement}")
    print(f"Money: ${user_money}")

def calculate():
    global user_money
    print("Please insert coins")
    for coins in money:
        money[coins] = int(input(f"How many {coins}?: "))
    user_money = (money["quarters"] * 0.25) + (money["dimes"] * 0.1) + (money["nickels"] * 0.05) + (money["pennies"] * 0.01)

def check_resource(coffee_type):
    is_sufficient = True
    for items in resources:
        for coffee in MENU[coffee_type]["ingredients"]:
            if items == coffee:
                if resources[items] < MENU[coffee_type]["ingredients"][coffee]:
                    is_sufficient = False
    return is_sufficient

def use_resource(coffee_type):
    for items in resources:
        for coffee in MENU[coffee_type]["ingredients"]:
            if items == coffee:
                resources[items] = resources[items] - MENU[coffee_type]["ingredients"][coffee]

def balance_restart():
    global user_money
    user_money = 0
    for coins in money:
        money[coins] = 0

while not game_end:
    user_input = input("What would you like? espresso/latte/cappuccino: ").lower()
    if user_input == "off":
        game_end = True
    elif user_input == "report":
        report()
    elif user_input == "esporesso" or "latte" or "cappuccino":
        calculate()
        if user_money >= MENU[user_input]["cost"]:
            if check_resource(user_input) is True:
                print(f'Here is ${round(user_money - MENU[user_input]["cost"], 2)} in change')
                print(f"Here is your {user_input}☕ enjoy")
                use_resource(user_input)
                balance_restart()
            else:
                print("Sorry there is not enough resource. Money refunded")
        else:
            print("Sorry that's not enough money. Money refunded")
            balance_restart()