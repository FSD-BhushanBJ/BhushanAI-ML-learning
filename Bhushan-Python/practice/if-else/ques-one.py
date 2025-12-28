print("Welcome to Movie Theatre")

age = int(input("Enter your age :"))

price = 0

if age <= 5:
        print("Entry fee is free")
elif age <= 12:
        price = 100
elif age <= 60:
        price = 150
else:
        price = 80

want = input("You want 3d glasses :")
if want == "y":
    price += 50

print(f"Your ticket is {price}")
