from main import MENU,report,resources
profit = 0
is_on = True

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def is_transaction_successful(money_received,drink_cost):
    """Return True when payment is accepted, or False when money is sufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2 )
        print(f"Here is the change {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("That's not enough money. Money Refunded")
        return False

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your Drink {drink_name}☕")

while is_on:
    choice = input("What would ou like to have?(espresso/latte/cappuccino)\n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"coffee: {resources["coffee"]}gm")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])





"""from idlelib.configdialog import changes

from main import MENU,report

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
earnings = 0
coffee_maker_function = True

def reports():
    return (f"{"Water: " + str(report["water"])+"ml"}\n"
            f"{"Milk: " + str(report["Milk"])+"ml"}\n"
            f"{"Coffee: " + str(report["coffee"]) + "gm"}\n"
            f"{"Money: " + str(report["Money"]) + "$"}\n"
            )
def drinks(cost):
    return MENU[cost]["cost"]


def process_coin(quarters_val,dimes_val,nickles_val,pennies_val,choice):
    total_coin_value = quarters_val + dimes_val + nickles_val + pennies_val
    change = total_coin_value - drinks(choice)
    return round(change,2)

while coffee_maker_function:
    choice = input("What would ou like to have?(espresso/latte/cappuccino)\n").lower()
    if choice == "report":
        print(reports())
    elif choice in MENU:
        quarters_val = int(input("How many quarters: ")) * quarters
        dimes_val = int(input("How many dimes: ")) * dimes
        nickles_val = int(input("How many nickels: ")) * nickles
        pennies_val = int(input("How many pennies: ")) * pennies
        earnings += quarters_val + dimes_val + nickles_val + pennies_val
        change = process_coin(quarters_val,dimes_val,nickles_val,pennies_val,choice)



        if change > 0:
            print(f"Here is the change ${change}")
        else:
            print("Sorry, not enough money. Money refunded.")
    else:
        print("Invalid choice")"""







