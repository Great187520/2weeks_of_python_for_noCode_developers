""" #Math Library
import math
print(math.sqrt(16))

#Factorial
print(math.factorial(5))

# Pi constant
print(math.pi) #Output: 3.14

#Random Library
import random

#Random interger between 1 and 10
print(random.randint(1, 10))

#Random choice from a List
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices)) #Output: Randomly selected fruit
 """
#Datetime Library
from datetime import datetime
#get current date and time
now = datetime.now()
print(now)

#Format date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date )

#Os Library
import os
print(os.getcwd())

print(os.listdir())

#create a directory

""" mypackage/
    __init__.py
    module1.py
    module2.py """

#structuring larger projects
""" project/
    main.py
    mypackage/
        __init__.py
        module1.py
        subpackage/
            __init__.py
            module2.py """

#Simple Calcuator using math library

import math

def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    
    choice = input("Select an operation (1-5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero.")
    elif choice == '5':
        num = float(input("Enter a number: "))
        print(f"Square Root: {math.sqrt(num)}")
    else:
        print("Invalid selection.")

calculator()
