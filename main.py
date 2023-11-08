MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money_options = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
resources = {"water": 300, "milk": 200, "coffee": 100}
machine_money = 0
report = f"Your Current Resources are as follows:\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: $ {machine_money}"

repeat_2 = True
while repeat_2:
    # Print drinks available with prices
    print (f"\nWelcome to our Fab Coffee Machine!\nPlease find below a list of our Fab drinks! \nEspresso for $ {MENU['espresso']['cost']} \nLatte for $ {MENU['latte']['cost']} \nCappuccino for $ {MENU['cappuccino']['cost']} \n")

    #Recieve User Input for the drink
    repeat = True
    while repeat:
        user_drink = input("What would you like to have for a drink?").lower() #either espresso, latte or cappuccino


    #Compare the user drink with the available resources: if enough proceed, if not send sorry message, Repeat
        for resource in resources:
    # Create an option to check available resources
            if user_drink == "report":
                print(report)
                repeat = True
                break
            if user_drink == "exit":
                exit()
            elif resources[resource] > MENU[user_drink]["ingredients"][resource]:
                repeat = False
            else:
                print(f"\nApologies, for any inconvenience but there are no enough {resource} in the machine currently! Please come again later!\n")
                repeat = True
                break

    #Request money from the user
    repeat_1 = True
    while repeat_1:
        print("Please Insert Coins..")
        quarters = int(input("How many Quarters?"))
        dimes = int(input("How many Dimes?"))
        nickles = int(input("How many Nickles?"))
        pennies = int(input("How many Pennies?"))
        user_money = quarters*money_options["quarters"]+dimes*money_options["dimes"]+nickles*money_options["nickles"]+pennies*money_options["pennies"]

        #Compare money with the price: if enough proceed & Return change, if not send sorry message, Repeat
        if user_money >= MENU[user_drink]["cost"]:
            change = round(user_money - MENU[user_drink]["cost"],2)
            print (f"Your Change is $ {change}")
            repeat_1 = False
        else:
            print(f"Your total money received is $ {user_money} and your {user_drink} costs $ {MENU[user_drink]['cost']}. Please Try Again!")

    #Add Money, Deduct resources, Repeat, Make coffee
    print (f"Here you go! The Best {user_drink} for our Fav Customer! See you Soon!")
    for resource in resources:
        resources[resource] -= MENU[user_drink]["ingredients"][resource]
    machine_money += user_money-change
    report = f"Your Current Resources are as follows:\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: $ {machine_money}"
