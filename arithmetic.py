""" add_two_number = 2 + 10
print(add_two_number) """

""" #Subtraction(-)
minus_two_number = 10 - 4
print(minus_two_number) """

""" #multiplication(*)
times = 7*4
print(times) """

""" #Division(/)
divide = 10/2
whole = int(divide)
print(whole) """

""" #Floor Division(//) (returns an integer quotient)
result = 10//3
print(result) """

""" #Modulus (%) (returns the remainder)
result = 10%3
print(result) """

""" #Equal(==)
result = (5==4)
print(result) """

""" #Not Equal (!=)
result = (5 != 4)
print(result) """

""" #Logical Operators
#AND  (and)
result = (3 > 5 and 8 < 10)
print(result) """

""" T F
1 1 True 
0 1 False
1 0 False
0 0 False """

""" #OR (or):
result = (5>3 or 10 < 8)
print(result)
 """
""" T F
1 1 True
1 0 True
0 1 True
0 0 False """

""" #NOT (not)
result = not(5>3)
print(result) """

""" y = 4 > 6
x = not(y)
print(x) """

""" #Concatenation
first_name = " John"
last_name = "Doe"
full_name = first_name +" "+last_name
print(full_name) """

""" s='abcdefghij'
slice = s[1:5]
print(slice) """

""" #python
#01234 
[]
z = 'Python'
y = z[2]
print(y) """

s = 'LovecityGosp'
#index: 0 1 2 3 4 5 6 7 8 9 10 11
#letter L o v e c i t y G o s  p 
""" y = s[2:5]
print(y) #output vec

y = s[:4]
print(y) """

""" y = s[:]# print entire code
print(y) """

""" y = s[-2:] #last 2 charaters from the end
print(y) """

""" y = s[1:7:2]
print(y) """

""" y = s[: : -1] #negative step reverses the string
print(y) """

#String Formatting
#Using f-strings
""" name = "John"
greeting = f"Hello, {name}!"
#f"{}"
print(greeting)
 """

""" #using .format()
age = 25
statement = " I am {} years old".format(age)
print(statement) """

#convert and calculate
""" Prompt the user to enter two numbers, convert them to integers, and calculate their sum """
""" num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#convert strings to integers
sum_result = int(num1) + int(num2)
print(sum_result)
print(f"The sum is: {sum_result}") """

#Temperature Converter
""" Write a program that converts a temperature from Fahrenheit to Celsius using the formula:
Celsius = (Fahrenheit - 32) * 5/9. """
fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * (5/9)
print(f"{fahrenheit}F is {celsius: .2f} C")

#String Manipulation
""" Create a program that prompts the user for their name and prints it in reverse order: """
""" name = input("Enter your name: ")
print(f"Your name reversed is: {name[::-1]}") """