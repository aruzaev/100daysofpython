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

height = float(input("Enter your height: "))
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
    print(f"Your BMI is {bmi}, you are clinically obese.")