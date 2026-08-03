from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def display(self):
        pass
class BankAccount(Person):
    total_accounts = 0

    def __init__(self, name, account_no, balance):
        super().__init__(name)
        self.account_no = account_no
        self.__balance = balance
        BankAccount.total_accounts += 1
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully.")
    def check_balance(self):
        print("Current Balance:", self.__balance)
    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.__balance)
    def display(self):
        self.display_details()
    @classmethod
    def show_total(cls):
        print("Total Accounts:", cls.total_accounts)
    @staticmethod
    def bank_rules():
        print("\n----- Bank Rules -----")
        print("Minimum Balance : 1000")
        print("Working Days    : Monday - Friday")
        print("Bank Hours      : 9 AM - 5 PM")
        print("Interest Rate   : 5%")
class SavingAccount(BankAccount):
    pass
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self):
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))

        if account_no in self.accounts:
            print("Account already exists.")
            return
        account = SavingAccount(name, account_no, balance)
        self.accounts[account_no] = account
        print("Account created successfully!")

    def search(self):
        account_no = int(input("Enter Account Number: "))
        if account_no in self.accounts:
            return self.accounts[account_no]
        else:
            print("Account not found.")
            return None

    def deposit(self):
        account = self.search()
        if account:
            amount = float(input("Enter Deposit Amount: "))
            account.deposit(amount)

    def withdraw(self):
        account = self.search()
        if account:
            amount = float(input("Enter Withdrawal Amount: "))
            account.withdraw(amount)

    def display(self):
        account = self.search()
        if account:
            account.display()
bank = Bank()
while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Bank Rules")
    print("6. Total Accounts")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        bank.create_account()
    elif choice == 2:
        bank.deposit()
    elif choice == 3:
        bank.withdraw()
    elif choice == 4:
        bank.display()
    elif choice == 5:
        BankAccount.bank_rules()
    elif choice == 6:
        BankAccount.show_total()
    elif choice == 7:
        print("Thank you! Visit Again.")
        break
    else:
        print("Invalid choice.")