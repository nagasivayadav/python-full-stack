multiple inheritance problems
class Animal:
    def eat(self):
        print("Animal eats food")

class Bird:
    def fly(self):
        print("Bird can fly")

class Parrot(Animal, Bird):
    def speak(self):
        print("Parrot can speak")
p = Parrot()

p.eat()     
p.fly()     
p.speak()
=================================================2
class camera:
    def capture(self):
        print("taking photo")
class music :
    def plays(self):
        print("music plays")
c= camera()
m= music()
c.capture()
m.plays()
===============================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
emp = Employee("k.nagasiva", 21, 20000)
emp.display()
===========================================
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
class Result(Student):
    def __init__(self, name, marks):
        
        super().__init__(name, marks)
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
r = Result("nagasiva", 80)
==================================================
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def show_balance(self):
        print(f"Balance: {self.__balance}")
account = BankAccount(5000)
===============================================
class Wallet:
    def __init__(self):
        self.__money = 1000

    def show_money(self):
        print(f"Money: {self.__money}")

w = Wallet()
w.show_money()
print("w.__money")
=================================================
class BankAccount:
    def __init__(self):
        self.__balance = 10000
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
            print("Remaining Balance:", self.__balance)
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print("Current Balance:", self.__balance)
account=BankAccount()
account.withdraw(10001)
account.show_balance()
==============================================
class Library:
    def __init__(self):
        self.__available = True  
    def borrow_book(self):
        if self.__available:
            self.__available = False
            print("Book borrowed successfully.")
        else:
            print("Book is not available.")
class Book(Library):
    def __init__(self, title, author):
        super().__init__()  
        self.title = title
        self.author = author
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

b = Book("Python Programming", "ABC")

b.display()
b.borrow_book()
==============================
polymorphisum methods )(overriding)
class animal:
    def sound(self):
        print("animal sound")
class dog(animal):
    def sound(self):
        print("bark")
class dog(animal):
    def sound(self):
        print("bark")
class cat(animal):
    def sound(self):
        print("meow")
d=dog()
c=cat()
d.sound()
d.sound()
c.sound()
========================
class book:
    def place(self):
        print("books are placed")
class python_book(book):
    def place(self):
        print("opened book")
b=book()
bp=python_book()
b.place()
bp.place()
===============================

class dog:
    def sound(self):
        print("bark")
class cat:
    def sound(self):
        print("meow")
def make_sound(animal):
    animal.sound()
make_sound(dog())
make_sound(cat())
==========================================================
over loading
class cal:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj= cal()
print(obj.add(10,20,30))
==================================
anoter method
class cal:
    def add(self,a,b,c=0):
        return a+b+c
obj= cal()
print(obj.add(10,20))
===============================================
abstraction
from abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):

    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
r= rectangle(10,5)
r.area()
============================
from abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area =3.14 * self.radius * self.radius
        print("radius",self.radius)
        print("area of circle",area)
c=circle(5)
c.area()
================================
class triangle():
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        area=0.5 *self.base* self.height
        print("base of triangle",self.base)
        print("height of triangle",self.height)
        print("area of triangle",area)
t=triangle(20,10)
t.area()
=====================================================================
import modules 
print( modules.add(10,20))
print(modules.mulitply(20,30))
==========another method
import modules as m
if __name__=='__main__':
    print(m.add(5,6))
=============
import math 
print(dir(math))
help