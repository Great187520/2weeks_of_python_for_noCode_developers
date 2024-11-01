#Dictionaries and User input
person = {
    "name": "Alice",
    "age" : 25,
    "profession": "Engineer"
}

""" print(person["name"])
print(person.get("name"))
 """

#Adding, Removing, and Modifying Entries
#Adding or Modifying Entries
# add a new key.
""" person["address"] = "No 1 onyeabor"
print(person)

# modify Entries
person["name"] = "John"
print(person)

person["age"] = 30
print(person)

#Removing Entries
del person["profession"]
print(person)
 """
#age = person.pop("age")
""" print(person)

print(person.keys()) #Output: dict_keys(['name', 'address'])
print(person.values()) #output: dict_values(['John', 'No 1 Onyeabor'])
print(person.items()) # output: dict_items([('name', 'John'), ('address', 'No 1 onyeabor')])
 """
#Nested Dictionaries
students = {
    "student1": {
        "name" :"John",
        "age": 22
    },
    "student2": {
        "name": "jane",
        "age": 23
    }
}

""" print(students["student1"]["age"], students["student2"]["name"])
print(students) """

#Practical use case of dictionaries
products = {
    "apple": 0.5,
    "banana": 0.3,
    "cherry": 1.5
}
#print(products["apple"])

#User input
#the input() function
name = input("Enter your name: ")
age = int(input("Enter your age:  "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote")