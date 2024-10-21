#Question1
# class car:
#     brand1="MG"
#     Model1="Hector"
#     brand2="Maruti"
#     Model2="Dzire"
#     Year="2022"
#     color="Black"
# car1= car()
# car2=car()
# print(car1.Model1)
# print(car1.brand1)
# print(car2.brand2)
# print(car2.Model2)
# print(car2.Year)
# print(car1.color)
#Question2
# class student:
#     def __init__(self,rollnumber,name,marks):
#         self.rollnumber=rollnumber
#         self.name = name
#         self.marks=marks
#     def info(self):
#         print(f"Name:{self.rollnumber}")
#         print(f"Name:{self.name}")
#         print(f"Name:{self.marks}")
# St1=student(25,"Abhay",78)
# St1.info()
# St2=student(75,"Ab",82)
# St2.info()
# St3=student(10,"Sanjay",90)
# St3.info()
#Question3
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth = breadth
#     def area(self):
#         return(self.length*self.breadth)
#
#     def perimeter(self):
#         return(2*((self.length)+(self.breadth)))
# rect1=Rectangle(10,5)
# rect2 =Rectangle(3, 7)
# rect3 = Rectangle(25, 5)
# rect4 = Rectangle(15, 7)
# print("Area:",rect1.area())
# print("Area:",rect2.area())
# print("Area:",rect3.area())
# print("Area:",rect4.area())
# print("Perimeter:",rect1.perimeter())
# print("Perimeter:",rect2.perimeter())
# print("Perimeter:",rect3.perimeter())
# print("Perimeter:",rect4.perimeter())
#Question4
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return((self.radius**2)*(3.14))
#     def circumfrence(self):
#         return(self.radius*2*3.14)
# ar1=Circle(10)
# cr1=Circle(10)
# print ("Area:",ar1.area())
# print("circumfrenc:",cr1.circumfrence())
# ar2=Circle(6)
# cr2=Circle(7)
# print ("Area:",ar2.area())
# print("circumfrenc:",cr2.circumfrence())
#Question5:
# class Account:
#     def __init__(self, accountn, balancec=0):
#         self.accountn = accountn
#         self.balancec = balancec
#
#     def debit(self, amount):
#         if amount > self.balancec:
#             print("Insufficient balance")
#         else:
#             self.balancec -= amount
#             print(f"Debited: {amount}. Balance_c: {self.balancec}")
#
#     def credit(self, amount):
#         self.balancec += amount
#         print(f"Credited: {amount}. updated Balance_c: {self.balancec}")
#
#     def print_balancec(self):
#         print(f"Account No: {self.accountn}, Balance_c: {self.balancec}")
#
# account1 = Account("555888000", 500)
# account1.print_balancec()
# account1.credit(1700)
# account1.debit(500)
# account1.print_balancec()
#Question6
# class Employee:
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         cls.employee_count += 1
#
#     @classmethod
#     def get_employee_count(cls):
#         return cls.employee_count
#
# employee1 = Employee(input("input the name1 :"))
# employee2 = Employee(input("input the name2 :"))
# employee3 = Employee(input("input the name3 :"))
# employee4 = Employee(input("input the name4 :"))
#
# print(f"Total employees: {Employee.get_employee_count()}")
#Question7
# class Book:
#     def __init__(self, title, author, price=0.0):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display_details(self):
#         print(f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price}")
# book1 = Book((input("Name of Book(title) :")),(input("Author :")), (int(input("Price of book :"))))
# book1.display_details()

#Question8
# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         return (celsius * 9/5) + 32
# converter = TemperatureConverter()
# temperatures_in_celsius = [50, 15, 20, 75, 90 ,80,72]
# for tempt in temperatures_in_celsius:
#     fahrenheit = converter.celsius_to_fahrenheit(tempt)
#     print(f"{tempt}°C is {fahrenheit}°F")
#Question9
# class Time:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#
#     def add_time(self, othertime):
#         total_minutes = self.minutes + othertime.minutes
#         total_hours = self.hours + othertime.hours + total_minutes // 60
#         total_minutes = total_minutes % 60
#         return Time(total_hours, total_minutes)
#
#     def display_time(self):
#         print(f"Time: {self.hours} hours and {self.minutes} minutes")
#
# time1 = Time(5, 20)
# time2 = Time(6, 10)
# result_time = time1.add_time(time2)
#
# result_time.display_time()

# #Question10:
# class EmployeeSalary:
#     basic_salary = 0
#     bonus_percentage = 0
#
#     def __init__(self, basic_salary):
#         self.basic_salary = basic_salary
#
#     @classmethod
#     def set_bonus_percentage(cls, bonus_percentage):
#         cls.bonus_percentage = bonus_percentage
#
#     def calculate_total_salary(self):
#         bonus_amount = (self.basic_salary * EmployeeSalary.bonus_percentage) / 100
#         return self.basic_salary + bonus_amount
#
# # Set the bonus percentage for all employees
# EmployeeSalary.set_bonus_percentage(7)
#
# employee1 = EmployeeSalary(7000)
# employee2 = EmployeeSalary(9500)
# employee3 = EmployeeSalary(12000)
#
# print(f"Total salary for employee 1: {employee1.calculate_total_salary()}")
# print(f"Total salary for employee 2: {employee2.calculate_total_salary()}")
# print(f"Total salary for employee 2: {employee3.calculate_total_salary()}")



























