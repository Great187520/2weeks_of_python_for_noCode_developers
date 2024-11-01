#lists, Tuples, and Sets

""" number = [1,2,3,4]
matrix = [[1,2], [2,3],[4,5]] """

#indexing and slicing lists
""" fruits = ["apple", "banana", "cherry"] """
""" print(fruits[0]) #output: apple
print(fruits[1:3]) #output: ['banana', 'cherry']
print(fruits[-1]) #Output: cherry """

#Modifying lists
#adding items
# append() and insert()
#using append()
""" fruits.append("orange")
print(fruits)

#using insert()
fruits.insert(2, "cashew")
#list_variable.insert(index value, list item)
print(fruits) """

#removing items
# remove(), pop(), clear()
# remove()
#fruits.remove("banana") #['apple', 'cherry']
#print(fruits)

#pop to remove an item by it's index:

""" fruits.pop(2) #output ['apple', 'banana']
print(fruits) """

""" #clear() to remove all elements
fruits.clear() #output: []
print(fruits)
 """

#Sorting Lists
#sort() to sort the list in ascending order

""" numbers = [3, 1, 4, 1, 5, 8]
numbers.sort()
print(numbers) #output: [1,1,3,4,5,8]

#sorting in descending order
numbers.sort(reverse=True)
print(numbers) """

#List Comprehensions
""" [ <expression> for <element> in <iterable> ]
There's also an optional 'if' condition:
[ <expression> for <element> in <iterable> if <condition> ] """
""" squares = [x**2 for x in range(10)]
print(squares) """

""" squares = [x**2 for x in (1,2,3,4)]
print(squares)

squares = []
for x in (1,2,3,4):
    squares.append(x**2)
print(squares) """

""" evens = [x for x in range(10) if x % 2 == 0]
print(evens) #Output: [0, 2, 4, 6, 8]

evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)
 """
#Tuples
""" colors = ("red", "green", "blue")

#accessing tuple elements
print(colors[0]) #Output: red
print(colors[1:]) #output: ('green', 'blue') """

#Tuple unpacking
""" person = ("John",25, "Engineer")
name, age, profession = person
print(name)
print(age)
print(profession) """

#Sets
#numbers = {1, 2, 3, 4, 5}

""" numbers = {1,2,2,3}
print(numbers) #Output: {1, 2, 3}

#Set Operations
#adding elements
numbers.add(6)
print(numbers) """

""" numbers.remove(3)
print(numbers) """

""" numbers.discard(3)
print(numbers) """

#mathematical set operations
#union: Combines all unique elements from two sets.
""" set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) """
#print(union_set) #output: {1,2,3,4,5}

#intersection
""" Returns elements common to both sets. """
""" intersection_set = set1.intersection(set2) """
#print(intersection_set) #output: {3}

#Difference
""" Returns elements present in the first set but not in the second. """
""" difference_set = set2.difference(set1)
print(difference_set)  """#output: {1, 2}
#Practical Exercises
#Filtering Data from a List
#Ex1 Removing Duplicates from a List
""" numbers = [1,2,3,4,2,5,3]
unique_numbers = list(set(numbers))
print(unique_numbers) """

#Ex2  Finding the Intersection of Two Lists

""" list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements) #Output [3,4] """

#Sorting and Filtering with list comprehensions
#Ex3: Sorting a list of dictionaries

""" people = [
    {"name":"Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

sorted_people = sorted(people, key=lambda x: x["age"])
print(sorted_people) """

#Ex 4: Filtering Even Numbers from a list
""" numbers = [1,2,3,4,5,6]
evens = [x for x in numbers if x % 2 == 0]
print(evens) """

#Using sets for fast membership testing
#Ex 5: Finding missing items

all_items = {"apple", "banana", "cherry", "date"}
purchased_items = {"apple", "banana"}

missing_items = all_items - purchased_items
print(missing_items)