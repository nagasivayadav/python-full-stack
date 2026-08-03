def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def division(a,b):
    if b==0:
        return"cannot divide by zero"
    return a/b
def modulus(a,b):
    if b== 0:
        return "cannot divide by zero"
    return a%b
def power(a,b):
    return a**b
while True:
    print("1.Addition")
    print("2.multiplication")
    print("3.subtraction")
    print("4.division")
    print("5.modulus")
    print("6.power")
    print("7.exit")

    choice = int(input("enter a choice:"))

    if choice == 7:
        print("calculator closed")
        break

    if choice < 1 or choice > 7:
        print("Invalid input")
        continue
    num1 =float(input("enter a number:"))
    num2 =float(input("enter a number:"))
    if choice == 1:
        print("result:",add(num1,num2))
    elif choice == 2:
        print("result:",multiply(num1,num2))
    elif choice == 3:
        print("result:",subtract(num1,num2))
    elif choice == 4:
        print("result:",division(num1,num2))
    elif choice == 5:
        print("result:",modulus(num1,num2))
    elif choice == 6:
        print("result:",power(num1,num2))




