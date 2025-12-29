print("Welcome to Python Pizza DeliverFest")

size = input("What size pizza do you want? S, M or L: ")

peri_peri = input ("Do you want periperi on your pizza? Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0

if size == "s":
    price = 15
elif size == "m":
    price = 20
elif size == "l":
    price = 25
else:
    price("Please select valid size")
if peri_peri == "y":
    if size == "s":
        price +=2 
    else:
        price +=3

if extra_cheese == "y":
    price +=1

total = price

print(f"Your total bill is ${total}")
    