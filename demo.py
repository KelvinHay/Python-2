

# Lets make a robot Barista
# She will have a name
# She will greet the customers
# She will offer a menu 
# She will collect the order
# Collect payment 
# Alert the customer when the order is complete 


MenuItems = "Black Coffee \n Cappuccino \n Frapuccino \n Latte \n"

PriceBlackCoffee = 3
PriceCappuccino = 4
PriceFrapuccino = 5
PriceLatte = 6


ReadyToOrder = input("Welcome to Coffee World!!! \n My name is Robot Barista. \n Are you ready to order? \n")

if ReadyToOrder == "No" or ReadyToOrder == "n" or ReadyToOrder == "NO" or ReadyToOrder == "no":
    IsReadyToOrder = input("Type 'Ready' when you want to order! \n")
    if IsReadyToOrder == "Ready" or IsReadyToOrder == "ready" or IsReadyToOrder == "READY":
        MenuItems = input("Great here is our menu: \n" + MenuItems + "What would you like to order? \n")

else:
    MenuItems = input("Great here is our menu, what would you like to order?: \n" + MenuItems)

if MenuItems == "Black Coffee" or MenuItems == "black coffee":
    Sugar = input("Would you like sugar?\n")
    if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
        PriceBlackCoffee = PriceBlackCoffee + 1
    Milk = input("Would you like cream?\n")
    if Milk == "Yes" or Milk == "yes" or Milk == "YES":
        PriceBlackCoffee = PriceBlackCoffee + 1
    Quantity = input("How many would you like to order?\n")
    PriceBlackCoffee = PriceBlackCoffee * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceBlackCoffee))

if MenuItems == "Cappuccino" or MenuItems == "cappuccino":
    Sugar = input("Would you like sugar?\n")
    if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
        PriceCappuccino = PriceCappuccino + 1
    Milk = input("Would you like cream?\n")
    if Milk == "Yes" or Milk == "yes" or Milk == "YES":
        PriceCappuccino = PriceCappuccino + 1
    Quantity = input("How many would you like to order?\n")
    PriceCappuccino = PriceCappuccino * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceCappuccino))

if MenuItems == "Frapuccino" or MenuItems == "frapuccino":
    Sugar = input("Would you like sugar?\n")
    if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
        PriceFrapuccino = PriceFrapuccino + 1
    Milk = input("Would you like cream?\n")
    if Milk == "Yes" or Milk == "yes" or Milk == "YES":
        PriceFrapuccino = PriceFrapuccino + 1
    Quantity = input("How many would you like to order?\n")
    PriceFrapuccino = PriceFrapuccino * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceFrapuccino))

if MenuItems == "Latte" or MenuItems == "latte":
    Sugar = input("Would you like sugar?\n")
    if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
        PriceLatte = PriceLatte + 1
    Milk = input("Would you like cream?\n")
    if Milk == "Yes" or Milk == "yes" or Milk == "YES":
        PriceLatte = PriceLatte + 1
    Quantity = input("How many would you like to order?\n")
    PriceLatte = PriceLatte * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceLatte))

OrderAgain = input("Would you like to order anything else? \n")




if OrderAgain == "Yes" or OrderAgain == "yes" or OrderAgain == "YES" or OrderAgain == "y":
    MenuItems = input("Great here is our menu: \n" + MenuItems + "What would you like to order? \n")

    if MenuItems == "Black Coffee" or MenuItems == "black coffee":
        Sugar = input("Would you like sugar?\n")
        if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
            PriceBlackCoffee = PriceBlackCoffee + 1
        Milk = input("Would you like cream?\n")
        if Milk == "Yes" or Milk == "yes" or Milk == "YES":
            PriceBlackCoffee = PriceBlackCoffee + 1
    Quantity = input("How many would you like to order?\n")
    PriceBlackCoffee = PriceBlackCoffee * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceBlackCoffee))

    if MenuItems == "Cappuccino" or MenuItems == "cappuccino":
        Sugar = input("Would you like sugar?\n")
        if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
            PriceCappuccino = PriceCappuccino + 1
        Milk = input("Would you like cream?\n")
        if Milk == "Yes" or Milk == "yes" or Milk == "YES":
            PriceCappuccino = PriceCappuccino + 1
    Quantity = input("How many would you like to order?\n")
    PriceCappuccino = PriceCappuccino * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceCappuccino))

    if MenuItems == "Frapuccino" or MenuItems == "frapuccino":
        Sugar = input("Would you like sugar?\n")
        if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
            PriceFrapuccino = PriceFrapuccino + 1
        Milk = input("Would you like cream?\n")
        if Milk == "Yes" or Milk == "yes" or Milk == "YES":
            PriceFrapuccino = PriceFrapuccino + 1
    Quantity = input("How many would you like to order?\n")
    PriceFrapuccino = PriceFrapuccino * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceFrapuccino))

    if MenuItems == "Latte" or MenuItems == "latte":
        Sugar = input("Would you like sugar?\n")
        if Sugar == "Yes" or Sugar == "yes" or Sugar == "YES":
            PriceLatte = PriceLatte + 1
        Milk = input("Would you like cream?\n")
        if Milk == "Yes" or Milk == "yes" or Milk == "YES":
            PriceLatte = PriceLatte + 1
    Quantity = input("How many would you like to order?\n")
    PriceLatte = PriceLatte * int(Quantity)
    print("Here is your order: \n" + MenuItems + "\n$" + str(PriceLatte))
else:
    print("Your order is complete!")
#    print("Your order is complete! your total is $" + str(PriceBlackCoffee + PriceCappuccino + PriceFrapuccino + PriceLatte))


    

