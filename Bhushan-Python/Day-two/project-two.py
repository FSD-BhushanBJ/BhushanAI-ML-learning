print("Welcome to the tip calculator!")

#input for bill amount
bill =int(input("What was the total bill ?\n$"))

#input for tip amount
tip = int(input("How much tip would you like to give? 10,12 or 15?\n"))

#calculates tip for bill amount
total_tip = bill * tip / 100

#calculates total bill + total tip
total_bill = total_tip + bill


#input for split the bill between how many people 
people = int(input("How many people to slipt the bill?\n"))

#split the between people according bill
split = total_bill/people 

#final anwser
print(f"Each person should pay : ${split} ")

