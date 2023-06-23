""" print("Welcome to the Tip Calculator")

totalBill = input("What was the total bill? $") # float
billSplits = input("How many people to split the bill? ") # int
tipPercentage = input("What percentage tip would you like to give? 10, 12, or 15? ") # float

# get how much each person is going to pay without the tip  

indivPayment = ((float(totalBill) / int(billSplits)) * (1 + (float(tipPercentage)) / 100)) # tipPercentage is 12.0 not 1.12 which makes the number wrong

print(f"Each person should pay: ${indivPayment:.2f}") """

""" height = input("Enter your height: ")
weight = input("Enter your weight: ")

bmi = (int(float(weight) / (float(height) ** 2)))

print(f"Your BMI is: {bmi}") """

age = input("What is your current age? ")

ageInDays = (90 * 365) - (int(age) * 365)
ageInWeeks = (90 * 52) - (int(age) * 52)
ageInMonths = (90 * 12) - (int(age) * 12)
print(f"You have {ageInDays} days, {ageInWeeks} weeks, and {ageInMonths} left.")