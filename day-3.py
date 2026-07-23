a=lambda x: x**2
print(a(5))
a=lambda x: x//2
print(a(5))
a=lambda x: x/2
print(a(5))
=====================================================
a=[1,10,30,9,60,20,25,5]
b=list(filter(lambda x: x%2 ==0,a))
c=list(map(lambda x: x**2,a))
print(b)
print(c)
================================================
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n - 1)

print(fact_rec(8))
========================
# feb
def fib(n):
        if n == 0 or n == 1:
            return n
        return fib(n - 1) + fib(n - 2)

print(fib(1))
================================================
s={1,2,3,4,4,5,8}

s.add(9)
s.remove(9)
s.discard(99)
print(s)
=======================================
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a | b)
print(a & b)
print(a -b)
print(a ^ b)
dictonary
student={'name':'nagasiva','age':20,'course':'mca'}
print(student['age'])
print(student.get('name',0))
student['city']='hydrabad'
student.pop(['city'])
print(student)
=================================
student={'name':'nagasiva','age':20,'course':'mca'}
print(student['age'])
print(student.get('name',0))
student['city']='hydrabad'
del student['city']
student.update({'number':9014085983})
print(student)

student.pop(['city'])
print(student)
==================================
set=(1,2,4,5,6,6,7,8)
print(set)
student={'naga':90,
         'ramu':87,
         'raju':67,
         'rahul':89
         }
for k v
s='hello world'
print(s[0])
print(s[::2])     
s.upper()         
print(s.upper())        
print(s.title())
print(s.strip())
print(s.lstrip())
print(s.lstrip())
print(s.replace('hello','python'))
print(s.find('python'))
print(s.count('1'))
print(len(s))
print(s.startswith('ll'))
print(s.endswith('ld'))
==========================
string function
name='name'; age=22
print({name},{age})
====================================
file=open('note.txt','w')
file.write("hello")
file.write("world")
file.close()
file=open('note.txt','r')
for line in file:
    print(line.strip())
file.close()
content = file.read()
print(content)
file.close()
with open('note.txt','a') as f:
    file.write('\n new line')
text = input("Enter a string: ")

print("Vowels found:")

for ch in text:
    if ch.lower() in "aeiou":
        print(ch)
=====================================
try :
    num =int(input("enter a number:"))
    Result = 100/num
    print(Result)
except ZeroDivisionError:
    print("error: cannot divide by zero")
except ValueError:
    print("error: enter a valid number")
else:
    print("success:",Result)
finally:
    print("executioon completed!")
======================================================
def validate_phone(phone):
    if len(phone) !=10:
        raise ValueError(f'phone must hava 10 digits!')
    return True
try:
    validate_phone('1234567890')
except ValueError as e:
    print('error',e)
=======================================

    