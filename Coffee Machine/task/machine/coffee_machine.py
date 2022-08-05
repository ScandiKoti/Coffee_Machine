supplies = {"water": 400, "milk": 540, "coffee_beans": 120, "disposable_cups": 9, "money": 550}
ingredients_for_coffee = {"water": [250, 350, 200], "milk": [0, 75, 100], "coffee_beans": [16, 20, 12],
                          "disposable_cups": [1, 1, 1], "money": [-4, -7, -6]}
ingredients = ["water", "milk", "coffee_beans", "disposable_cups", "money"]


def condition():
    print(f"""The coffee machine has:
{supplies["water"]} ml of water
{supplies["milk"]} ml of milk
{supplies["coffee_beans"]} g of coffee beans
{supplies["disposable_cups"]} disposable cups
${supplies["money"]} of money""")


def buy():
    coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if coffee not in ["1", "2", "3", "back"]:
        print("U-u-ups")
    elif coffee == "back":
        coffee_machine()
    elif coffee in ["1", "2", "3"]:
        coffee = int(coffee)
    for i in ingredients:
        if supplies[i] < ingredients_for_coffee[i][coffee - 1]:
            print(f"Sorry, not enough {i}!")
            coffee_machine()
    print("I have enough resources, making you a coffee!")
    for i in ingredients:
        supplies[i] -= ingredients_for_coffee[i][coffee - 1]


def fill():
    supplies["water"] += int(input("Write how many ml of water you want to add:\n"))
    supplies["milk"] += int(input("Write how many ml of milk you want to add:\n"))
    supplies["coffee_beans"] += int(input("Write how many grams of coffee beans you want to add:\n"))
    supplies["disposable_cups"] += int(input("Write how many disposable cups you want to add:\n"))


def take():
    print(f"I gave you ${supplies.get('money')}")
    supplies["money"] = 0


def coffee_machine():
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            condition()
        elif action == "exit":
            exit()


coffee_machine()
