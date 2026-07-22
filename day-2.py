# a=int(input("enter the subject1:"))
# b=int(input("enter the subject2:"))
# c=int(input("enter the subject3:"))
# total=a+b+c
# average=total//3
# print("total marks:",total)
# print("average marks :",average)
# if average >40:
#     print("pass")
# else:
#     print("fail")
#     ========================================
# bills=int(input("enter electricity bill no:"))
# if bills <=100:
#     bill= bills*5
# elif bills <=200:
#     bill= (100*5)+ ((bills-100 )*7)
# else:
#     bill=(100 * 5)+(100 *7)+((bills - 200)* 10)

# print(bill)
# ===============================================

# atm withdrwas

# 4 ============================
# a=int(input("enter marks:"))
# b=int(input("enter b marks:"))
# c=int(input("enter c marks:"))
# total = a+b+c
# average= total/3
# if average >= 90:
#     print("A")
# elif average>= 75:
#     print("B")
# elif average >=60:
#     print("C")
# elif average >= 40:
#     print("D")
# else:
#     print("fail")

# print("average is :",average)
# print("total marks:",total)
# =================================
# num=int(input("enter a number:"))
# reverse=0
# while num <=0:
#     digit= num %10
#     reverse= reverse * 10 + digit
#     num = num//10
# print("reversed the number:",reverse)
# a=int=(input("enter the numbers:"))
# for i in range(1,6):
#     if i % 2==0 :
#         print("even digits:")
#     else:
#         print("odd digits:")
# ==============================================
# username="nagasiva"
# password="Naga"
# user=(input("enter user name:"))
# pas=(input("enter the password:"))
# if user == username and pas == password:
#     print(" login sucessfully!")
# else:
#     print("invalid user!")

# ====================secret number========
# ///
# # discount
# username="nagasiva"
# password="Naga@1234"
# a=input("enter user name:")
# b=input("enter password:")
# if a == username and b == password:
#     print("login into user")
# else:
#     print("invalid password") 
# ===================================

# price = float(input("Enter the price of the laptop: "))


# if price >= 50000:
#     discount_percent = 20 
# elif price >= 30000:
#     discount_percent = 10 
# else:
#     discount_percent = 5   

# discount_amount = (price * discount_percent) / 100
# final_price = price - discount_amount


# print(f"Discount Percentage: {discount_percent}%")
# print(f"Discount Amount: ${discount_amount}")
# print(f"Final Amount to Pay: ${final_price}")
# ====================================================================
# a=int(input("enter"))
# num = int(input("Enter a number: "))
# temp = num
# rev = 0

# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# ===============================================================
# def leap_year():
#     a=int(input("enter a leap year:"))
#     if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
#         print("it is a leap year")
    
#     else:
#         print("it is a not leap year")
# leap_year()

# a=int (input("enter leap year:"))
# if a % 400 ==0 or a % 4==0 and a% 100!=0:
#     print("it is leap year")
# else:
#     print("its not a leap year")
# =====================================================================
balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter a number: "))

    if choice == 1:
        print("Current balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        balance = balance + amount
        print("New balance:", balance)

    elif choice == 3:
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdraw successful.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")





    