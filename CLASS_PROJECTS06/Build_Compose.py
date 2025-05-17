# Step-by-Step Python OOP Assignments with Editable Sections

# --- 1. Using `self` ---
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# 👇 Your explanation or notes:
# (What does self do? Why is it needed?)

if __name__ == "__main__":
    print("Assignment 1: Using self")
    s1 = Student("Ali", 88)
    s1.display()
    input("Q: What does 'self' represent inside a class? Your answer: ")


# --- 2. Using `cls` ---
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 2: Using cls")
    Counter()
    Counter()
    Counter.show_count()
    input("Q: How many objects were created and how does 'cls' help in tracking them? Your answer: ")


# --- 3. Public Variables and Methods ---
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting...")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 3: Public Variables and Methods")
    car = Car("Honda")
    print(f"Car Brand: {car.brand}")
    car.start()
    input("Q: Is 'brand' a public variable and can it be accessed directly? Your answer: ")


# --- 4. Class Variables and Class Methods ---
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 4: Class Variables and Class Methods")
    print(f"Old Bank Name: {Bank.bank_name}")
    Bank.change_bank_name("New Horizon Bank")
    print(f"New Bank Name: {Bank.bank_name}")
    input("Q: How does 'cls' work with class variables to change values across all instances? Your answer: ")


# --- 5. Static Methods ---
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 5: Static Methods")
    print("Sum of 5 and 7:", MathUtils.add(5, 7))
    input("Q: What is a static method and when would you use one? Your answer: ")


# --- 6. Constructors and Destructors ---
class Logger:
    def __init__(self):
        print("Logger object created")

    def __del__(self):
        print("Logger object destroyed")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 6: Constructors and Destructors")
    logger = Logger()
    del logger
    input("Q: When is a constructor and destructor triggered in a class? Your answer: ")


# --- 7. Access Modifiers ---
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 7: Access Modifiers")
    emp = Employee("Ali", 50000, "XYZ123")
    emp.show_info()
    input("Q: Which attributes are public, protected, and private? Can they be accessed directly? Your answer: ")


# --- 8. Using `super()` ---
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 8: Using super()")
    t = Teacher("Sarah", "Biology")
    print(f"Name: {t.name}, Subject: {t.subject}")
    input("Q: Why is 'super()' used in the child class constructor? Your answer: ")


# --- 9. Abstract Classes ---
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 9: Abstract Classes")
    rect = Rectangle(5, 4)
    print("Area:", rect.area())
    input("Q: What is an abstract method and why is it useful? Your answer: ")


# --- 10. Instance Methods ---
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 10: Instance Methods")
    d = Dog("Max", "Beagle")
    d.bark()
    input("Q: What is an instance method and how is it different from a class or static method? Your answer: ")


# --- 11. Class Methods ---
class Book:
    total_books = 0

    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 11: Class Methods")
    Book()
    Book()
    print("Total books:", Book.total_books)
    input("Q: How does a class method help manage class-level data like 'total_books'? Your answer: ")


# --- 12. Static Methods ---
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 12: Static Methods")
    print("0°C in Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(0))
    input("Q: Why would you use a static method instead of an instance method here? Your answer: ")


# --- 13. Composition ---
class Engine:
    def start(self):
        print("Engine started")

class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 13: Composition")
    engine = Engine()
    car = CarWithEngine(engine)
    car.start_car()
    input("Q: How is 'Engine' used inside 'CarWithEngine'? What is composition here? Your answer: ")


# --- 14. Aggregation ---
class EmployeeIndependent:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.employee = emp

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 14: Aggregation")
    emp = EmployeeIndependent("Ahmed")
    dept = Department(emp)
    print("Employee in Department:", dept.employee.name)
    input("Q: What is aggregation and how does this example show it? Your answer: ")


# --- 15. MRO / Diamond Inheritance ---
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 15: MRO / Diamond Inheritance")
    obj = D()
    obj.show()
    input("Q: Which 'show()' method gets called and why? Explain using MRO. Your answer: ")


# --- 16. Function Decorator ---
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 16: Function Decorator")
    say_hello()
    input("Q: What does a function decorator do and how is it used here? Your answer: ")


# --- 17. Class Decorator ---
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class PersonDecorated:
    pass

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 17: Class Decorator")
    p = PersonDecorated()
    print(p.greet())
    input("Q: What is the purpose of a class decorator and what does it add here? Your answer: ")


# --- 18. Property Decorators ---
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 18: Property Decorators")
    prod = Product(100)
    print(prod.price)
    prod.price = 150
    print(prod.price)
    del prod.price
    input("Q: How do @property, @setter, and @deleter work together in this class? Your answer: ")


# --- 19. __call__() and callable() ---
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 19: __call__() and callable()")
    m = Multiplier(4)
    print(m(5))
    print("Is m callable?", callable(m))
    input("Q: What does __call__() enable and how does callable() relate to it? Your answer: ")


# --- 20. Custom Exception ---
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 20: Custom Exception")
    try:
        check_age(16)
    except InvalidAgeError as e:
        print("Exception caught:", e)
    input("Q: What is a custom exception and why would you use one? Your answer: ")


# --- 21. Custom Iterable ---
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# 👇 Your explanation or notes:

if __name__ == "__main__":
    print("Assignment 21: Custom Iterable")
    for num in Countdown(3):
        print(num, end=" ")
    print()
    input("Q: How does the class support iteration and what methods are used? Your answer: ")


# --- Testing Code (Optional) ---
# You can comment out this block if you're doing step-by-step execution.



    print("Q2: How many Counter objects are created?")
    Counter()
    Counter()
    Counter.show_count()
    input("Your answer: ")

    print("Q3: Is 'brand' a public variable in Car class?")
    car = Car("Toyota")
    print(f"Car brand is: {car.brand}")
    car.start()
    input("Your answer: ")

    print("Q4: What does class method do in Bank?")
    print(f"Original Bank Name: {Bank.bank_name}")
    Bank.change_bank_name("XYZ Bank")
    print(f"Updated Bank Name: {Bank.bank_name}")
    input("Your answer: ")

    print("Q5: What is a static method?")
    print("Sum:", MathUtils.add(5, 7))
    input("Your answer: ")

    print("Q6: When is constructor/destructor triggered?")
    temp_logger = Logger()
    del temp_logger
    input("Your answer: ")

    print("Q7: Can you access private, protected, and public variables?")
    emp = Employee("Ali", 50000, "XYZ123")
    emp.show_info()
    input("Your answer: ")

    print("Q8: How does 'super()' help in inheritance?")
    teacher = Teacher("Sarah", "Biology")
    print(teacher.name, teacher.subject)
    input("Your answer: ")

    print("Q9: What's the area of a rectangle?")
    r = Rectangle(3, 4)
    print("Area:", r.area())
    input("Your answer: ")

    print("Q10: What does the dog say?")
    dog = Dog("Max", "Beagle")
    dog.bark()
    input("Your answer: ")

    print("Q11: Class method to count books:")
    Book()
    Book()
    print(Book.total_books)
    input("Your answer: ")

    print("Q12: Convert 0°C to Fahrenheit:")
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    input("Your answer: ")

    print("Q13: Car with Engine Composition")
    engine = Engine()
    c = CarWithEngine(engine)
    c.start_car()
    input("Your answer: ")

    print("Q14: Aggregation Example")
    e = EmployeeIndependent("Nida")
    d = Department(e)
    print("Department employee:", d.employee.name)
    input("Your answer: ")

    print("Q15: Method Resolution Order in class D")
    d = D()
    d.show()
    input("Your answer: ")

    print("Q16: Function decorator output")
    say_hello()
    input("Your answer: ")

    print("Q17: Class decorator output")
    p = PersonDecorated()
    print(p.greet())
    input("Your answer: ")

    print("Q18: Property getter/setter")
    prod = Product(99)
    print(prod.price)
    prod.price = 120
    print(prod.price)
    del prod.price
    input("Your answer: ")

    print("Q19: Multiplier class with __call__")
    m = Multiplier(3)
    print(m(10))
    print("Is callable?", callable(m))
    input("Your answer: ")

    print("Q20: Custom exception check")
    try:
        check_age(16)
    except InvalidAgeError as e:
        print("Exception caught:", e)
    input("Your answer: ")

    print("Q21: Countdown Iterable")
    for n in Countdown(3):
        print(n, end=" ")
    print()
    input("Your answer: ")


