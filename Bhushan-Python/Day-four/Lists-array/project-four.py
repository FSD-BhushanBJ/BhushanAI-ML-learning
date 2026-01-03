import random
print("Welcome to the Rock, Paper & Scissors Game")



rock =  '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) rock'''

paper = '''
     _______
---'    ____)____1
           ______)
          _______)
         _______)
---.__________) paper'''

scissor = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) scissor'''



choice = int(input("0 for Rock\n 1 for paper\n 2 for scissors\n Enter you choice : "))
rand_no = [rock,paper,scissor]
com = random.randint(0,2)
print(rand_no[com])
print("your choice",choice)
print("Computer", com)

if choice == com:
    print("Draw")
    
elif choice == 0 and com == 2: 
    print("You Won")

elif choice == 1 and com == 0:
    print("YOU WON")

elif choice == 2 and com == 2:
    print("you won")
elif choice in [0,1,2]:
    print("you lose")
else:
    print("Please enter valid number")



