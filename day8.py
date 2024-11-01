""" class Dog:
    A simple attempt to model a dog.

    def __init__(self, name, age):
        Initialize name and age
        self.name = name
        self.age =age

    def sit(self):
        Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")

my_dog = Dog('Bingo', 5)
#Dog('Bingo',5).sit()
my_dog.sit()
my_dog.roll_over() """

""" class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

my_car = Car("Benz", "GLE", "2025")
my_car.display_info() """

#Encapsulation
""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!"
            )
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount('John Doe', 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance()) #Output 1200 """

#Inheritance
""" class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print("The vehicle is starting.")

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, year)
        self.model = model

    def honk(self):
        print("The car is honking.")

my_car = Car("Toyota", "Corolla", 2020)
my_car.start()
my_car.honk()

 """

#Polymorphism
""" class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
    

class Cat(Animal):
    def sound(self):
        return "Meow"
    
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound()) """

#Abstraction
""" Abstraction involves hiding the internal implementation details of an object and only exposing the essential features. In Python, abstraction can be achieved using abstract classes. """

#Example 1: E-commerce system
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product: {self.name}, Price: ${self.price}")

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    def remove_item(self, product):
        self.items.remove(product)
        print(f"Removed {product.name} from the cart.")

    def total_price(self):
        return sum(item.price for item in self.items )
    
product1 = Product("Laptop", 1200)
product2 = Product("Headphones", 150)

cart = ShoppingCart()
cart.add_item(product1)
cart.add_item(product2)

print(f"Total price: ${cart.total_price()}")