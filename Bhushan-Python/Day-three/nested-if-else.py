print("Welcome to the rollercoaster !")

height = int(input("What is your height is cm? "))

#using greater than equals to match height
#if else condition
if height >= 120:
    print("You can ride the rollercoaster")

    #input for age
    age = int(input("Enter your age :"))

    #using nested if elif to charge money according to age
    if age <= 12:
        print("You have to pay $5")
    elif age <= 18 :
        print("You have to pay $7")
    else:
        print("You have to pay %12")
else:
    print("Sorry you have to grow taller before you can ride.")