import packages.basic as 
import packages.adavance as a

print(p.add(10,20))
print(a.multiply(10,20))
============================
import packages.basic as *


print(basic.add(10,20))
print(basic.multiply(10,20))
===================================
from packages import add
from packages import multiply

print(add(10,20))
print(multiply(10,20))
==========================================================
from packages.students import student
from packages.marks import mark

print(student("name",99))
print(mark(90,99,100))
=============================================
import pandas as pd
data={
    "name":["name1","name2","name3"],
    "age":[22,23,24]

}
df= pd.DataFrame(data)
print(df)
================================================
    =====================================================
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My Game")
running = True
while running:
    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), (250, 250), 50)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
========================================
import pandas as pd
data={
    "name":["name1","name2","name3"],
    "age":[22,23,24]

}
df= pd.DataFrame(data)
print(df)
==============================================
plat
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 8, 6, 10, 9]

plt.plot(x, y, marker='o')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
==================================================
scatter plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 8, 6, 10, 9]

plt.scatter(x, y, marker='o')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
=========================================
pie
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 8, 6, 10, 9]

plt.pie(x, y)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
==============================================
class Count:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
for n in Count(15):
    print(n)
=================================================
generators
def fruits():
    yield "apple"
    yield "orange"
    yield "grape"
    yield "banana"
g=fruits()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
=====================================================
def even(n):
    for i in range(2,n+1,2):
        yield i
for num in even(20):
    print(num)
    ==============================
def even(n):
    for i in range(1,n+1):
        yield i ** 2
for num in even(5):
    print(num)
==========================================
def even(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
for num  in even(10):
    print(num)
======================================================
def decarator_function(n):
    def wrapper():
        print("before function")
        n()
        print("after function")
    return wrapper

@decarator_function
def greet(name):
    print("hello",name)
    
greet("hello")
========================================
import pandas as pd
data ={
    'name':{'naga','siva','chan'},
    'marks':{89,78,98}

}
df= pd.DataFrame(data)
print(df)