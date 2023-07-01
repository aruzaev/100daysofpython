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

# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")

# r = int(position[0]) - 1
# c = int(position[1]) - 1

# map[r][c] = "x"

# print(f"{row1}\n{row2}\n{row3}")

import random

moves = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
outcomes = ["win", "lose", "tie"]

# print(moves[2] + "\nYou " + outcomes[0])

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
pcChoice = random.randint(0, 2)

if pcChoice == playerChoice:
    print(moves[playerChoice] + "\nComputer chose:" + moves[pcChoice] + "\nYou " + outcomes[2])

elif (pcChoice == 0 and playerChoice == 2) or (pcChoice == 2 and playerChoice == 1) or (pcChoice == 1 and playerChoice == 0):
    print(moves[playerChoice] + "\nComputer chose:" + moves[pcChoice] + "\nYou " + outcomes[1])

elif (playerChoice == 0 and pcChoice == 2) or (playerChoice == 2 and pcChoice == 1) or (playerChoice == 1 and pcChoice == 0):
    print(moves[playerChoice] + "\nComputer chose:" + moves[pcChoice] + "\nYou " + outcomes[0])
    