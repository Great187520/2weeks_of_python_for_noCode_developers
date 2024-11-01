#Conditional Statements
# The if Statement
""" age = 25

if age >= 18:
    print("You are eligible to vote")
else:
    print("under age") """

#elif statement
#else if

""" score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F") """

#Else

""" temp = 25

if temp > 30:
    print("It's hot!")
elif temp > 20:
    print("It's warm")
else:
    print("it's cold")

 """

""" #While Loop
count = 1

while count <= 5:
    print(f"Count is {count}")
    count = count + 1
    #count += 1 """

#The for Loop
""" fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}") """


""" for i in range(5):
    print(i) """

""" for i in range(10):
    print('Hello') """

""" for hi in range(5):
    print("hi") """


""" #Nested Condition
for num in range(1,6):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd") """

#Nested Loops
""" matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#[[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    for element in row:
        print(element)
 """
#Break, continue, and Pass Statements
""" Sometimes you need more control over your loops. Python offers the break, continue, and pass statements to manage the flow within loops. """

#break Statement
""" break exits the loop entirely, skipping any remaining iterations. """
""" for num in range(1, 11):
    if num == 5:
        break
    print(num) """

""" celsuis = float(input("enter temp in celsuis: "))
fahrenheit =(celsuis*(9/5)) + 32
print(f"{celsuis: .2f}C is {fahrenheit}F") """

#continue Statement
""" for num in range(1, 6):
    if num == 3:
        continue
    print(num) """

""" #pass Statement
for num in range(1, 6):
    if num == 3:
        pass #Do nothing for now
    print(num) """
""" # Sending Reminder Emails
clients = ["alice@example.com", "bob@example.com", "carol@example.com"]

for client in clients:
    print(f"Sending email to {client}")
    print("i have sent you an email")
 """

#processing files in a directory
""" import os

#directory = "/path/to/files"
directory = "/Users/HP ELITEBOOK 830 G5/Pictures"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(f"Processing {filename}")
 """

#simple Calculator
""" Write a program that takes two numbers and an operator (+, -, *, /) from the user and performs the corresponding operation. """

""" num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, / ): ")

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Invaild operator")
 """

#Multiplication Table
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}")
        
    print()