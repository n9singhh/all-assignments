#Question1

# class MathOperations:
#     staticmethod
#     def add(a,b):
#         return(a+b)
#     print(add(5,9))
#     staticmethod
#     def add(a, b):
#         return (a * b)
#     print(add(6, 4))


# #Question2
#
# class Person:
#     # Class variable to keep track of the number of instances
#     count = 0
#
#     def __init__(self):
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# a = Person()
# b = Person()
# c = Person()
# d = Person()
# e = Person()
# print(f"Total number of people: {Person.get_count()}")
#Question3
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
#     @classmethod
#     def info(cls):
#         return
# temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(10)
# info_message = TemperatureConverter.info()
#
# print(f"0°C is {temp_in_fahrenheit}°F")
# print(info_message)

#Question4

# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class dog(Animal):
#     def sound(self):
#         print("Bark")
# generic_animal = Animal()
# generic_animal.sound()
# dog = dog()
# dog.sound()

#Question6:
# class bird:
#     def fly(self):
#         print("flying")
#
# class fish:
#     def swim(self):
#         print("swimming")
#
# class duck(bird, fish):
#     pass
#
# Duck = duck()
# Duck.fly()
# Duck.swim()


#Question6
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, breadth, length):
#         self.breadth= breadth
#         self.length = length
#
#     def area(self):
#         return self.breadth* self.length
#
# # Example usage:
# circle = Circle(10)
# rectangle = Rectangle(5, 5)
#
# print(f"Area of the circle: {circle.area():.2f}")
# print(f"Area of the rectangle: {rectangle.area()}")

#Question7
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: {amount}. New balance: {self._balance}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrawn: {amount}. New balance: {self._balance}")
#         else:
#             print("Insufficient balance or invalid withdrawal amount.")
#
#     def get_balance(self):
#         return self._balance
# account = BankAccount(5000)
# account.deposit(1500)
# account.withdraw(3000)
# print(f"Current balance: {account.get_balance()}")

# #Question 8: "
#
# class Dog:
#     def bark(self):
#         print("Woof")
#
# class Cat:
#     def speak(self):
#         print("Meow")
#
# dog = Dog()
# cat = Cat()
#
# dog.bark()
# cat.speak()

#Question 9:

# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
#
# calc = Calculator()
#
# result_2_args = calc.add(200, 40)
# print(f"Sum of two numbers: {result_2_args}")
#
# # Add three numbers
# result_3_args = calc.add(50, 40, 50)
# print(f"Sum of three numbers : {result_3_args}")

#Question10:

# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
#
# human = Human()
# human.breathe()
# human.walk()
# human.think()




