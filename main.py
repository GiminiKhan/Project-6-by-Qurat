   # Project 6 Build Compose and Decorate A Complete OOP Practice Series

# 1. Using Self
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = student("Qurat", 95)
student1.display()

print("\n---\n")

# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_counter()

print("\n---\n")

# 3. Public variables and methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...!")

my_car = Car("Audi")
print(my_car.brand)
my_car.start()

print("\n---\n")

# 4. Class variables and Class Methods
class Bank:
    bank_name = "Metropolitan Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

account1 = Bank("Ammara")
account2 = Bank("Sara")

account1.display()
account2.display()

Bank.change_bank_name("Qurat Bank")

account1.display()
account2.display()

print("\n---\n")

# 5. Static variables and static methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(10, 5)
print("The sum of my 2 numbers is:", result)

print("\n---\n")

# 6. Logger with constructor and destructor messages
class Logger:
    def __init__(self):
        print("Message Before: Logger object created.")

    def __del__(self):
        print("Message After: Logger object destructor.")

log = Logger()
del log

print("\n---\n")

# 7. Access Modifiers: Public, Protected, Private
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public
        self._salary = salary      # protected
        self.__ssn = ssn           # private

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive in number")

    def get_ssn(self):
        return self.__ssn

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter command: {self.get_ssn()}")

m = Manager("Ali", 12000, "428-777-1845", "Information Technology")
m.show_manager_info()
m.set_salary(32000)
print("Updated Salary:", m._salary)

print("\n---\n")

# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

t = Teacher("Qurat", "Python Course")

print("\n---\n")

# 9. Abstract Class and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(6, 10)
print("Area of Rectangle:", rect.area())

print("\n---\n")

# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says : Woof Woof!")

dog1 = Dog("Shaggy", "Tommy")
dog1.bark()

print("\n---\n")

# 11. Class Methods
class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Brave New World", "Aldous Huxley")

print("Total number of books:", Book.get_total_books())

print("\n---\n")

# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

print("\n---\n")

# 13. Composition
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP is starting."

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_car(self):
        return f"{self.brand} car: {self.engine.start()}"

engine1 = Engine(150)
car1 = Car("Toyota", engine1)
print(car1.start_car())

print("\n---\n")

# 14. Aggregation
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_department_info(self):
        return f"Department: {self.dept_name}\n{self.employee.get_details()}"

emp1 = Employee("Alice", 101)
dept1 = Department("HR", emp1)
print(dept1.show_department_info())

print("\n---\n")

# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        return "Showing from class A"

class B(A):
    def show(self):
        return "Showing from class B"

class C(A):
    def show(self):
        return "Showing from class C"

class D(B, C):
    pass

d = D()
print(d.show())
print("Method Resolution Order:", [cls.__name__ for cls in D.__mro__])

print("\n---\n")

# 16. Function Decorators
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

print("\n---\n")

# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.greet())

print("\n---\n")

# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Getter: Retrieve the price"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: Update the price"""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter: Delete the price attribute"""
        print("Deleting price...")
        del self._price

product = Product(100)
print("Price:", product.price)

product.price = 150
print("Updated Price:", product.price)

del product.price

# Uncommenting the next line will raise an error because price is deleted
# print(product.price)

print("\n---\n")

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

mult = Multiplier(5)
print("Is mult callable?", callable(mult))
print("Result of mult(10):", mult(10))

print("\n---\n")

# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"InvalidAgeError: Provided age {age} is less than 18.")
    else:
        print(f"Age {age} is valid.")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Caught an exception:", e)

try:
    check_age(21)
except InvalidAgeError as e:
    print("Caught an exception:", e)

print("\n---\n")

# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

for number in Countdown(5):
    print(number)
