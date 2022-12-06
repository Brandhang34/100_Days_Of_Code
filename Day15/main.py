#Dictionary of the Menu
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

#Dictionary of resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Global variable Money to keep track how much the coffee machine received
money = 0

#Function to print the report of the coffee machine
def print_report(resources):
    print(f"Water:",resources["water"], "ml")
    print(f"Milk:",resources["milk"], "ml")
    print(f"Coffee:",resources["coffee"], "g")
    print(f"Money: $",round(money,2))

#Function to convert a given amount of coins into $
def insert_convert_coins():
    coins = []
    coins.append(round(float(input("how many quarters?: ")) * .25, 2))
    coins.append(round(float(input("how many dimes?: ")) * .10, 2))
    coins.append(round(float(input("how many nickel?: ")) * .05, 2))
    coins.append(round(float(input("how many pennies?: ")) * .01, 2))
    return sum(coins)

#Function to check if resources in the coffee machine is available
def check_resources(type, coins):
    global money
    if type == "espresso":  #type of coffee is espresso
        if coins <  MENU["espresso"]["cost"]: #Checks if there are not enough funds
            print("Sorry, that's not enough money. Money refunded")
            return
        elif resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]: #Checks if there are enough resources
            print("Sorry, there's not enough resources. Money refunded")
            return "no resources"
        else:
            resources["water"] -= MENU["espresso"]["ingredients"]["water"] #subtracts the resources
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"] 
            money += MENU["espresso"]["cost"] #adds money given to the machine
            if coins > MENU["espresso"]["cost"]: #Gives the change back to the user
                change = round(coins - MENU["espresso"]["cost"],2)
                print(f"Here is ${change}, in change")
            print(f"Here is your {type}. Enjoy!")
    elif type == "latte":
        if coins <  MENU["latte"]["cost"]:
            print("Sorry, that's not enough money. Money refunded")
            return
        elif resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] or resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, there's not enough resources. Money refunded")
            return"no resources"
        else:
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            money += MENU["latte"]["cost"]
            if coins > MENU["latte"]["cost"]:
                change = round(coins - MENU["latte"]["cost"],2)
                print(f"Here is ${change}, in change")
            print(f"Here is your {type}. Enjoy!")
    elif type == "cappuccino":
        if coins <  MENU["cappuccino"]["cost"]:
            print("Sorry, that's not enough money. Money refunded")
            return
        elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"] or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"] or resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, there's not enough resources. Money refunded")
            return "no resources"
        else:
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            money += MENU["cappuccino"]["cost"]
            if coins > MENU["cappuccino"]["cost"]:
                change = round(coins - MENU["cappuccino"]["cost"],2)
                print(f"Here is ${change}, in change")
            print(f"Here is your {type}. Enjoy!")

machine_on = True
while(machine_on):
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        print_report(resources)
    elif user_input == "espresso":
        if check_resources(user_input,insert_convert_coins()) == "no resources":
            break

    elif user_input == "latte":
        if check_resources(user_input,insert_convert_coins()) == "no resources":
            break
    elif user_input == "cappuccino":
        if check_resources(user_input,insert_convert_coins()) == "no resources":
            break
    elif user_input == "off":
        machine_on = False
    else:
        print(f"Invalid input. Try again.")
    