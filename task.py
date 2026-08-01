try:
    a=float(input("enter a number:"))
    b=float(input("enter b number:"))
    print("result",a/b)

except ZeroDivisionError:
    print("error: division zero is not allowed")
except ValueError:
    print("error: division should only numeric values")
============================================================
class employe:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)

emp1=employe("nagasiva",40000)
emp2=employe("mohan",35000)
emp1.display()
print()
emp2.display()
=================================================================
3rd questioni
import math
class shape:
    def __init__(self):
        pass
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length* self.width
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius ** 2
r=rectangle(10,5)
c=circle(3)
print("rectangle is ",r.area)
print("circle is",c.area)
=======================================================
4 th question
class dog:
    def speak(self):
        return "dog says bow"
class cat:
    def speak(self):
        return "cat say meow"
def describe(animal):
    print(animal.speak())
describe(dog())
describe(cat())
===============================
5 th question
class bank_account:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount >=0:
            self.__balance = amount
        else:
            print("invalid balance")
acc=bank_account(10000)
print("account balance is",acc.get_balance())
acc.set_balance(2000)
print("updated balance",acc.get_balance())
=======================================================
6th question
import utility
print("addition",utility.add(10,20))
print("multiply",utility.subtract(20,30))
=======================================================
8th question
def even_number():
    n=0
    while True:
        yield n
        n +=2
gen = even_number()
for _ in range(10):
    print(next(gen))
=================================================================
9th question
import time
def timer(fun):
    def wraps(*args,**kwargs):
        start=time.time()
        result=fun(*args,**kwargs)
        end= time.time()
        print("execution time:",end - start,"seconds")
        return result
    return wraps
@timer
def simple():
    for i in range(100000):
        pass
simple()
============================================================
10 question
def positive_num(fun):
    def wrapper(*args):
        if all( x >0 for x in args):
            return fun(*args)
        else:
            print("all argements must be positive")
    return wrapper
@positive_num
def multiply(a,b):
    print("product:",a *b)
multiply(5,6)
multiply(-2,4)
=============================================
11 th question
import os
files= os.listdir()
print("text files:")
for file in files:
    if file.endswith(".txt"):
        print(file)
================================================
12th question
import math
radius=float(input("enter radius:"))
Area= math.pi * radius **2
circumference =2 * math.pi * radius
print("area:",Area)
print("circumference",circumference)
==============================================
13 question
from datetime import datetime
dob = input("Enter DOB (YYYY-MM-DD): ")
birth = datetime.strptime(dob, "%Y-%m-%d")
today = datetime.today()
age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1
print("Age:", age)
========================================================
14th question
import sys
total =5
for ar in sys.argv[1:]:
    try:
        total += float(ar)
    except ValueError:
        pass
print("sum",total)
===========================================
15 th question
def tower_of(n,source,au,destination):
    if n==1:
        print(f" move disk 1 from{source} to {destination}")
        return 
    tower_of(n -1,source,destination,au)
    print(f"move disk{n}from{source} to {destination}")
    tower_of(n-1,au ,source,destination)
n=int(input("enter number of disks:"))
tower_of(n,'A','B','C')
===========================================================
16 th question
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter N: "))
print("Fibonacci:", fibonacci(n))
==========================================================
17 th question
products={
    "laptap": 60000,
    "phone":50000,
    "tv":45000,
    "watch": 10000,
    "tablet":350000
}
top3 = sorted(products.items(),key=lambda x:x[1],reverse=True)[:3]
print("top 3 most expensive products:")
for name, price in top3:
    print(name, ":",price)
====================================================================
18 th question
set1= set(map(int,input("enter first set:").split()))
set2= set(map(int,input("enter second set:").split()))
print("union:",set1 | set2)
print("intersection",set1 & set2 )
print("difference (set1 - set2):",set1 - set2)
========================================================
19 th question
from collections import Counter
with open("inpu.txt","r") as file:
    text = file.read().lower().split()
Count = Counter(text)
top5= Count.most_common(5)
with open("output.txt","w") as file:
    for word, freq in top5:
        file.write(f"{word}: {freq}\n")
print("top 5 words t  output.txt")
=========================================================================
20 th question
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    print("Valid age.")

try:
    age = int(input("Enter age: "))
    validate_age(age)
except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid integer.")


