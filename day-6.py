# multiple inheritance problems
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
# =================================================2
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
# ===============================================
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
# ===========================================
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
class Result(Student):
    def __init__(self, name, marks):
        
        super().__init__(name, marks)
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
# r = Result("nagasiva", 80)
# ==================================================
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def show_balance(self):
        print(f"Balance: {self.__balance}")
account = BankAccount(5000)
# ===============================================
class Wallet:
    def __init__(self):
        self.__money = 1000

    def show_money(self):
        print(f"Money: {self.__money}")

w = Wallet()
w.show_money()
print("w.__money")
# =================================================
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