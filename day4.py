import random

""" randInt = random.randint(0, 1)

if randInt == 1:
    print("Heads")
else:
    print("Tails") """
""" 
names_string = input("Give me everybody's name, separated by a comma. ")
names = names_string.split(", ")

payee = random.randint(0, len(names))

print(names[payee] + " is going to buy the meal today!") """

""" fruits = ["Strawberries", "Nectarines", "Apples", "Grapes"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery"]

dirtyDozen = [fruits, vegetables]

print(dirtyDozen) """

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

coords = position.split()
print(coords)


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

