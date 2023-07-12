# fruits = ["Apple", "Pear", "Orange"]

# for i in range(0, len(fruits)):
#     print(str(i + 1) + ". " + fruits[i])

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# numberOfStudents = 0 
# totalHeight = 0

# for student in student_heights:
#     numberOfStudents += 1

# for height in student_heights:
#     totalHeight += height

# print(round(totalHeight / numberOfStudents))

# studentScores = input("Input a list of student scores ").split()

# for n in range(0, len(studentScores)):
#     studentScores[n] = int(studentScores[n])

# print(studentScores)

# highestScore = 0

# for i in studentScores:
#     if i > highestScore:
#         highestScore = i

# print(f"The highest score in the class is: {highestScore}")

# sum = 0

# for number in range(2, 101, 2):
#     sum += number

# print(sum)

# for number in range(1, 101):
#     if number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

totalChars = nr_letters + nr_numbers + nr_symbols

lettersList = []
symbolsList = []
numbersList = []

password = []


for i in range(0, nr_letters):
    lettersList.append(letters[random.randint(0, len(letters) - 1)])
    # get the number value of the array index for both letters, numbers
    # and symbols

    # attribute index to symbol 

    # ???

for i in range(0, nr_symbols):
    symbolsList.append(symbols[random.randint(0, len(symbols) -1)])

for i in range(0, nr_numbers):
    numbersList.append(numbers[random.randint(0, len(numbers) - 1)])

password = lettersList + symbolsList + numbersList

for i in range(0, len(password)):
    print(password[i], end="")

print(" ")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P