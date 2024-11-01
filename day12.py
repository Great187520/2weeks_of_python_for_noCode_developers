#Chapter 1: Introduction to Decorators and Lambda Functions
""" import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def compute_square(n):
    return n ** 2

print(compute_square(10))
 """
""" #Lambda Functions
add = lambda x, y: x + y
# def add(x,y):
    #return x + y
print(add(5, 3)) """

#numbers = [1, 2, 3, 4, 5]
"""
#Using map to square numbers
squared = list(map(lambda x: x**2, numbers))
print(squared)

#using filter to get even numbers
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers) """

#Understanding Python’s Built-in Functions and Advanced Data Handling Techniques

""" squared = [x ** 2 for x in numbers]
print(squared)

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
 """
#Dictionary Comprehensions

""" squared_dict = {x: x**2 for x in numbers}
print(squared_dict) """

#import json

""" with open("data.json", 'r') as file:
    data = json.load(file)
    print(data) """

""" data_to_write = {"name": "wick", "age": 30}
with open('output.json', 'w') as file:
    json.dump(data_to_write, file, indent=4) """

import csv

""" with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
 """

""" data_to_write = [["name", "age"], ["Alice", 25], ["Bob", 30]]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write) """


#Expense track
import json
from datetime import datetime

expenses = []

def add_expense(amount, category, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    expense = {"amount": amount, "category": category, "date": date }
    expenses.append(expense)

def view_expenses():
    for expense in expenses:
        print(f"{expense['date']}: {expense['category']} - ${expense['amount']}")

def export_to_json(filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file,  indent=4)

def generate_summary():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total}")

#Main program loop
while True:
    action = input("Choose an action (add/view/export/summary/exit): ").strip().lower()
    if action == 'add':
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        add_expense(amount, category)
    elif action == 'veiw':
        view_expenses()
    elif action == 'export':
        export_to_json()
        print("Expenses exported to JSON.")
    elif action == 'summary':
        generate_summary()
    elif action == 'exit':
        break
    else:
        print("Invalid action. please try again")
