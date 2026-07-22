# a=int(input("enter a value:"))
# b=int(input("enter a value:"))
# c=int(input("enter a value:"))
# if a>b and a>c:
#     print("a is the biggest number")
# elif b>a and b>c:

#     print("b is biggest number") 
# else:
#     print("c is big")

# print("hello")
# ===================================================
# a= int(input("enter a year"))
# if a % 400 ==0 :
#     print("it is a leap year")
# elif a % 4 ==0 & a% 100 != 0:
#     print("it is a leap year")
# else:
#     print("it is not a leap year")

# def leap_year():
#     a=int(input("enter a leap year:"))
#     if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
#         print("it is a leap year")
    
#     else:
#         print("it is a not leap year")
    # =========================================================

# leap_year()
# a=10
# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")
# else:
#     print("zero")
# def postive_num():
#     a=int(input("enter a number:"))
#     if a>0:
#         print("positive")
#     elif a<0:
#         print("negative")
#     else:
#         print("zero")
# postive_num()

# num = int(input("Enter a number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number:", reverse)
# # 

# list=[1,2,3,"name"]
# print(list)
# tuple=(1,2,3,"name")
# print(tuple)
# set={1,2,2,3,4,5,"name"}
# print(set)
# print(type)
# print(type(set))
# print(set)
# =========================
# a=int(input("enter a value:"))
# count=0
# for i in a:
#     count+1
# print(count)
# ======================
# a=int(input("enter a number:"))
# b=0
# while a>0:
#     a=a//10
#     b+=1
# print(b)
# =============================
#=
# a=int(input("enter a number:"))
# b=0
# for i in range(0,len(a)):
#     b=b+1
# print(b)
# a=int(input("enter a number:"))
# b=0
# while a>0:
#     a= a//10
#     b=-1
# print(b)

# ===============================
# num=[]


# for i in range(4):
#     num1=int(input())
#     num.append(num1)
# num.sort()
# print("third largest",num[-3])
# ===========================================
# a=int(input("enter a number:"))
# sum=0
# for i in range(a):
#     sum=sum + int(i)
# print(sum)
# username="nagasiva"
# password="Naga@1234"
# a=input("enter user name:")
# b=input("enter password:")
# if a == username and b == password:
#     print("login into user")
# else:
#     print("invalid password") 
#     =========================================
# n=int(input("enter a number:"))
# a=0
# b=1
# c=0
# while c<n:
#     d=a+b
#     a=b
#     d=d
# print(a)

# for i in range(1,5):
#     print("*"*i)

for i in range(100):
    if i % 2 ==0:
        print(i,end=" ") 