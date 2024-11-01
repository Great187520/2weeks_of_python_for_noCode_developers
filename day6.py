#Functions and Modular code
#what is a function?
def greet():
    print("Hello, World!")

#greet()

def greet(name):
    print(f"Hello, {name}!")

#greet("Victor")
#greet("Village people")

#Return Values and Scope
#Returning Values
""" def add(a, b):
    return a + b

result = add(3, 4) """
#print(result)

#Function Scope: Local vs Global Variables
#Local Variables 
""" Local Variables
Variables created inside a function exist only within that function’s scope. These are called local variables and cannot be accessed outside the function. """
""" x = 4

def example():
    x = 5
    print(x)

example()
print(x)
 """
#Global Variable
""" x = 10 # Global variable

def print_global():
    print(x) #Accessing global variable inside a function

print_global() # Output: 10 """

#Modifying Global Variables
""" x = 10

def modify_global():
    global x
    x = 5
    #print(x)

modify_global()
print(x) """

#DEfault Arguments
""" def greet(name="Stranger"):
    print(f"Hello, {name}!")

greet() #output: Hello, Stanger!
greet("Alice") #Output: Hello, Alice! """

#Keyword Arguments

""" def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="John")
introduce("Alice", 25)
introduce(40, "Wick") """

#Organizing code with functions
#Area Calulator

""" def area_of_circle(radius):
    return 3.14159 * radius ** 2

def area_of_rectangle(width, height):
    return width*height

def main():
    print("Choose a shape: 1 for  Circle,  2 for Rectangle")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is {area_of_circle(radius)}")
    elif choice == 2:
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        print(f"The area of the rectangle is {area_of_rectangle(width, height)}")
    else:
        print("Invaild choice!")

if __name__ == "__main__":
    main()
 """
""" import math_utils
result = math_utils.add(5, 3)
print(result) #Output: 8

result = math_utils.subtract(5, 3)
print(result)
 """
""" from math_utils import add, subtract

result = add(5, 3)
print(result) # Output: 8 """

import math
print(math.sqrt(16)) #Output: 4.0