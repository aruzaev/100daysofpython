""" number = int(input("What number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.") """

""" print("Welcome to the rollercoaster!")
height = int(input("Enter your height: "))

if height >= 120:
    age = int(input("How old are you? "))
    if age > 18:
        print("That will be $12")
    elif age <= 18:
        print("That will be $7")
    else:
        print("That will be $5")
else:
    print("You aren't tall enough to ride this ride") """

""" height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = round(float(weight / height**2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")   
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.") """
""" 
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.") """
""" 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
wantsPepperoni = input("Do you want pepperoni? Y or N ")
extraCheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if wantsPepperoni == "Y":
        bill += 2
    if extraCheese == "Y":
        bill +=1
elif size == "M":
    bill = 20
    if wantsPepperoni == "Y":
        bill += 3
    if extraCheese == "Y":
        bill +=1
elif size == "L":
    bill = 25
    if wantsPepperoni == "Y":
        bill += 3
    if extraCheese == "Y":
        bill +=1

    

print(f"Your final bill is: ${bill}") """

""" print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your their name? \n")

name1Lower = name1.lower()
name2Lower = name2.lower()

totalString = name1Lower + name2Lower

trueNumber = totalString.count("t") + totalString.count("r") + totalString.count("u") + totalString.count("e")
loveNumber = totalString.count("l") + totalString.count("o") + totalString.count("v") + totalString.count("e")

score = str(trueNumber) + str(loveNumber)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
 """

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

leftRightPrompt = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\". ").lower()

if leftRightPrompt == "right":
    swimOrWaitPrompt = input("You've come to a lake. There is an island in the middle of the lake. "
                             "Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
    if swimOrWaitPrompt == "wait":
        whichDoor = input("You arrive at the island unharmed. There is a house with 3 doors. "
                          "One red, one yellow and one blue. Which colour do you choose? ").lower()
        if whichDoor == "yellow":   
            print("You found the treasure! You win!")
        else:
            print("you died game over")
    else:
        print("You drowned, game over!")
else:
    print("You fucking died, game over bitch")