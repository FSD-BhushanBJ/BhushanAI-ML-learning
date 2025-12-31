states_of_india = ["Maharashtra","Gujarat","Madhya Pradresh","Kanartaka","Kerala","UttarPradresh"]

print("States :",states_of_india)
print("-------------------------------")
print(states_of_india[0])
print("-------------------------------")

#append funtion
states_of_india.append("Tamilnadu")
print(states_of_india)
print("-------------------------------")

#extend funtion
states_of_india.extend(["Odisha","Jharkand"])
print(states_of_india)
print("-------------------------------")

#insert function
states_of_india.insert(1,"Pakistan")
print(states_of_india)
print("-------------------------------")

#remove funtion is removing the item using string name
states_of_india.remove("Pakistan")
print(states_of_india)

print("-------------------------------")

#pop funtion is removing the item using indexing
states_of_india.pop(1)
print(states_of_india)

print("-------------------------------")

#clear funtions is delete the inside the list items not the variable
states_of_india.clear()
print(states_of_india)