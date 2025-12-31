import random

friends = ["Bhushan","Mayank","Shivani","Gaytri","Diksha"]

pay = random.randint(0,4)

print(f"Who will pay the bill today its :-",friends[pay])


#using choice function

print("-------------------------------")
print(random.choice(friends))