print("Welcome to the rollercoaster !")

height = int(input("What is your height is cm? "))
bill = 0

#using greater than equals to match height
#if else condition
if height >= 120:
    print("You can ride the rollercoaster")

    #input for age
    age = int(input("Enter your age :"))

    #using nested if elif to charge money according to age
    if age <= 12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18 :
        bill = 7
        print("You have to pay $7")
    # elif age >= 45 and age <= 55:
    elif 45 <= age <= 55:
        print("You can get free ride")
    else:
        bill = 12
        print("You have to pay %12")
    
    #input for extra charge for photo if user type yes or no
    print_extra = input("You have to pay extra 3$ for photos, if you 'Y' for Yes and 'N' for No :")

    if print_extra == "Y":
        bill += 3
    print(f"Your total bill is {bill}$")
    
else:
    print("Sorry you have to grow taller before you can ride.")