print("Welcome to Python Pizza Deliveries !")

size = input("What size pizza do you want ? S, M or L: ").lower()

papperoni = input("Do you want pepperoni ? Y or N: ").lower()

extracheese = input("Do you want extra cheese ? Y or N: ").lower()

price = 0



if size == "s":
    price = 15
elif size == "m":
    price = 20
elif size == 'l':
    price = 25 


if papperoni == "y":
    if size == "s":
        price += 2
    else:
        price += 3

if extracheese == "y":
    price  += 1

total = price


print(f"Your final bill is: ${total}")
