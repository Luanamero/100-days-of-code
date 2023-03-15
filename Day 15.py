
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

in_function = True
money = 0

while in_function:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"Money: {money}")
    elif coffee_choice == "espresso":
        if int(MENU["espresso"]["ingredients"]["water"]) > int(resources["water"]):
            print("Sorry there is not enough water.")
        elif int(MENU["espresso"]["ingredients"]["coffee"]) > int(resources["coffee"]):
            print("Sorry there is not enough coffee.")
        elif int(MENU["espresso"]["ingredients"]["water"]) <= int(resources["water"]) and int(MENU["espresso"]["ingredients"]["coffee"]) <= int(resources["coffee"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickels = int(input("How many nickels?")) * 0.05
            pennies = int(input("How many pennies?")) * 0.01
            costumer_money = quarters + dimes + nickels + pennies
            if costumer_money < int(MENU["espresso"]["cost"]):
                print("Sorry that's not enough money. Money refunded...")
            else:
                resources["water"] = int(resources["water"]) - int(MENU["espresso"]["ingredients"]["water"])
                resources["coffee"] = int(resources["coffee"]) - int(MENU["espresso"]["ingredients"]["coffee"])
                money += float(MENU["espresso"]["cost"])
                if costumer_money > int(MENU["espresso"]["cost"]):
                    change = round((costumer_money - float(MENU["espresso"]["cost"])), 2)
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your espresso. Enjoy!")
    elif coffee_choice == "latte":
        if int(MENU["latte"]["ingredients"]["water"]) > int(resources["water"]):
            print("Sorry there is not enough water.")
        elif int(MENU["latte"]["ingredients"]["coffee"]) > int(resources["coffee"]):
            print("Sorry there is not enough coffee.")
        elif int(MENU["latte"]["ingredients"]["milk"]) > int(resources["milk"]):
            print("Sorry there is not enough milk.")
        elif int(MENU["latte"]["ingredients"]["water"]) <= int(resources["water"]) and int(MENU["latte"]["ingredients"]["coffee"]) <= int(resources["coffee"]) and int(MENU["latte"]["ingredients"]["milk"]) <= int(resources["milk"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickels = int(input("How many nickels?")) * 0.05
            pennies = int(input("How many pennies?")) * 0.01
            costumer_money = quarters + dimes + nickels + pennies
            if costumer_money < int(MENU["latte"]["cost"]):
                print("Sorry that's not enough money. Money refunded...")
            else:
                resources["water"] = int(resources["water"]) - int(MENU["latte"]["ingredients"]["water"])
                resources["coffee"] = int(resources["coffee"]) - int(MENU["latte"]["ingredients"]["coffee"])
                resources["milk"] = int(resources["milk"]) - int(MENU["latte"]["ingredients"]["milk"])
                money += float(MENU["latte"]["cost"])
                if costumer_money > int(MENU["latte"]["cost"]):
                    change = round((costumer_money - float(MENU["latte"]["cost"])), 2)
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your latte. Enjoy!")
    elif coffee_choice == "cappuccino":
        if int(MENU["cappuccino"]["ingredients"]["water"]) > int(resources["water"]):
            print("Sorry there is not enough water.")
        elif int(MENU["cappuccino"]["ingredients"]["coffee"]) > int(resources["coffee"]):
            print("Sorry there is not enough coffee.")
        elif int(MENU["cappuccino"]["ingredients"]["milk"]) > int(resources["milk"]):
            print("Sorry there is not enough milk.")
        elif int(MENU["cappuccino"]["ingredients"]["water"]) <= int(resources["water"]) and int(MENU["cappuccino"]["ingredients"]["coffee"]) <= int(resources["coffee"]) and int(MENU["cappuccino"]["ingredients"]["milk"]) <= int(resources["milk"]):
            print("Please insert coins.")
            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickels = int(input("How many nickels?")) * 0.05
            pennies = int(input("How many pennies?")) * 0.01
            costumer_money = quarters + dimes + nickels + pennies
            if costumer_money < int(MENU["cappuccino"]["cost"]):
                print("Sorry that's not enough money. Money refunded...")
            else:
                resources["water"] = int(resources["water"]) - int(MENU["cappuccino"]["ingredients"]["water"])
                resources["coffee"] = int(resources["coffee"]) - int(MENU["cappuccino"]["ingredients"]["coffee"])
                resources["milk"] = int(resources["milk"]) - int(MENU["cappuccino"]["ingredients"]["milk"])
                money += float(MENU["cappuccino"]["cost"])
                if costumer_money > int(MENU["cappuccino"]["cost"]):
                    change = round((costumer_money - float(MENU["cappuccino"]["cost"])), 2)
                    print(f"Here is ${change} dollars in change.")
                    print("Here is your cappuccino. Enjoy!")

    elif coffee_choice == "off":
        in_function = False
