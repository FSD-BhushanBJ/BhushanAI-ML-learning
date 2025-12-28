print("Welcome to the rollercoaster !")

height = int(input("What is your height is cm? "))

#using greater than equals to match height
#if else condition
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")

    #input for age
    age = int(input("Enter your age :"))

    #using nested if elif to charge money according to age
    if age <= 12:
        bill = 5
        
    elif age <= 18 :
        bill = 7
       
    else:
        bill = 12
        

    photo_extra = input("Want Photo? :")

    if photo_extra == "y":
        bill += 3
    
    print(f"The total bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")