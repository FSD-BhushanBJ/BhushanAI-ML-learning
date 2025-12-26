weight = 85
height = 1.85


bmi = weight/(height**2)

#logic one
if bmi <= 18.5 :
    print("Underweight")
else :
    if bmi <= 29.9 :
        print("normal weight")
    else :
        print("Overweight")

print("------------------")

#logic two
if bmi <= 18.5:
    print("Underweight")
elif bmi <= 25:
    print("Normal weight")
else:
    print("Overweight")

print("------------------")

#always start if else with greater value
if bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal Weight")
else:
    print("Underweight")