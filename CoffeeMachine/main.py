from menu import *
# TODO 1: get user input for order at the beginning of service and every time order is completed
coffee_machine_on = True
welcome_message = f"Welcome to Simone's Cafe!"
print(welcome_message)


def generate_report():
    report = []
    for k, v in resources.items():
        if k == "coffee":
            report.append(f"{k}: {v}g")
        else:
            report.append(f"{k}: {v}ml")
    return f"{report[0]}\n{report[1]}\n{report[2]}"


def update_resources(coffee_choice):
    if coffee_choice == "espresso":
        resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    return


def check_resources(coffee_choice):
    if coffee_choice == "espresso":
        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"]:
            return True
    elif coffee_choice != "espresso":
        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"] and resources["milk"] >= MENU[coffee_choice]["ingredients"]["milk"]:
            return True


def process_coins(pound, fifty, twenty, ten, five, one):
    total = []
    money_processor = {
        "pounds": 1.00,
        "fifty_p": 0.50,
        "twenty_p": 0.20,
        "ten_p": 0.10,
        "five_p": 0.05,
        "one_p": 0.01
    }
    total.append(money_processor["pounds"] * pound)
    total.append(money_processor["fifty_p"] * fifty)
    total.append(money_processor["twenty_p"] * twenty)
    total.append(money_processor["ten_p"] * ten)
    total.append(money_processor["five_p"] * five)
    total.append(money_processor["one_p"] * one)

    return float(format(sum(total), ".2f"))


def process_change(money_input, coffee_price):
    if money_input > coffee_price:
        change = money_input - coffee_price
        return f"Your change is: £{change}"
    elif money_input < coffee_price:
        difference = coffee_price - money_input
        return f"Sorry you haven't paid enough, you need to insert £{difference} more"
    else:
        return "Thank you for supporting us. Hope you enjoy your coffee!"


# TODO 2: machine should switch off when user inputs "off"
while coffee_machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        coffee_machine_on = False
# TODO 3: a report should be generated for inventory when requested by user
    if user_input == "report":
        print(generate_report())
# TODO 4: check there are sufficient resources before making order
    if user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
        if check_resources(user_input):
            cost = MENU[user_input]['cost']
            reformatted_cost = float(format(cost, ".2f"))
            print(f"{user_input.title()} costs: £{reformatted_cost}, please insert your coins.")
            pounds = int(input("How many 1 pound coins are you entering?: "))
            fifty_p = int(input("How many 50 pence coins are you entering?: "))
            twenty_p = int(input("How many 20 pence coins are you entering?: "))
            ten_p = int(input("How many 10 pence coins are you entering?: "))
            five_p = int(input("How many 5 pence coins are you entering?: "))
            one_p = int(input("How many 1 pence coins are you entering?: "))
# TODO 5: process coins
            total_coins = process_coins(pounds, fifty_p, twenty_p, ten_p, five_p, one_p)
            print(f"You have inserted £{total_coins}")
# TODO 6: check user has inserted right amount of money. Too little return message, too much return change
            print(process_change(total_coins, reformatted_cost))
# TODO 7: if the user inserted the right amount, add info to report and print final message
            update_resources(user_input)
        else:
            print("Sorry this option is out of stock, please come back later.")
