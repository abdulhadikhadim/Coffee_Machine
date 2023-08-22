from data_file import MENU , resources, money

from art_data import intro_logo,end_logo,send_logo
def check_resources(ingredients):
    for data in ingredients:
        if ingredients[data] >= resources[data]:
            print(f"Sorry there is insufficient {data}")
            return False
    return True

def coins_calculation():
    print("Insert the Coins: ")
    total = int(input("How Many Number of Quarters:"))*0.25
    total += int(input("How Many Number of Dimes:")) * 0.10
    total += int(input("How Many Number of Nickles:")) * 0.05
    total += int(input("How Many Number of Pennies:")) * 0.01
    return total


def check_transection(payment , cost_received):
    if payment >= cost_received:
        change = round(payment - cost_received,2)
        print(f"Here is your ${change}")
        global money
        money += cost_received
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

print(intro_logo)
def make_coffe(drink_name , order_ingredient):
    for ingredients in order_ingredient:
        resources[ingredients] -= order_ingredient[ingredients]
    print(f"Here is your {drink_name} ☕☕😘. Enjoy it!")
    print(send_logo)


def main():
    is_next_customer = False
    while not is_next_customer:

        option = input("What would you like? (espresso/latte/cappuccino): ")
        if option == "off":
            print(end_logo)
            is_next_customer = True
        elif option == "report":
            print(f"Water: {resources['water']}")
            print(f"milk: {resources['milk']}")
            print(f"milk: {resources['coffee']}")
            print(f"money : {money}")
        else:
            drink = MENU[option]
            if check_resources(drink["ingredients"]):
                payment = coins_calculation()
                if check_transection(payment,drink["cost"]):
                    make_coffe(option , drink["ingredients"])
    input("Enter any key to exit: ")

main()





