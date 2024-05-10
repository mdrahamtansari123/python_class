# def addition():

# # in this part scoping
#     num1 = int(input("Enter a first number"))
#     num2 = int(input("Enter a second number"))
#     total = num1+num2
#     # print(f"Answer = {num1+num2}")
#     return total

# s = addition()
# print(s)

# def greet():
#     name = input("Enter your Name = ")
#     print(f"{name}")

# print("Ansari")

# greet()

#1. Without parameters, without return
#2. With parametres , with returns
#3. without parametres, with Return
#4. With Parameters , with Return

#1. Without parameters, without return

# Example

# def addition(num1,num2,): # this parameters
#      total_number = num1+num2
#      print(total_number)

# addition(4,5) # this Arguments

# Total number add in list
# def addition_list(x):

#      total = 0
#      for i in x:
#           total = total+i
#      print(total)
# my_list = [1,2,3,4,5]

# addition_list(my_list)

## Return , when will you do  use return  before store data in varible
# jb koi returns krati hai use variable me save krte hai then print krte hai ya fir directly prin kra skte hai

## jab koi variable dega use return krna pdega or use return karne ke liy ak object ko varialble me store krna hoga

# Example

# def add1(num1,num2):
#      total = num1+num2
#     #  return total
#      print(total)
# add1(23,45) ##This is no print

# s1 = add1(12,34)
# print(s1)

# print(add1(12,34))

# def add(n1,n2):
#     total = n1 + n2
#     # print(total)
    
#     return total

# def check(num):
#     if num%2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# x = int(input("Enter your first number = "))
# y = int(input("Enter your first number = "))

# s = add(x,y)
# print(s)

# check(s)

# def fun1():
#     x="hello world"
#     return x

# s = fun1()
# print(s)




# x=int(input("enter the first number="))
# y=int(input("enter the second number="))


# def sum1(x,y):
#     total = x+y
#     cheack(total)



# def cheack(total):
#     if total %2 == 0:
#         print(f"{total} Even number")
#     else:
#         print(f"{total} Odd")

# sum1(x,y)
# cheack(z)

# def add(n1,n2,n3,*args,**kwargs):
#     print(f"{n1=}")
#     print(f"{n2=}")
#     print(f"{n3=}")
#     print(f"{args=}")
#     print(f"{kwargs}")
#     print(kwargs["name"])

# add(2,3,4,8,79,8,8,name="Rahamat")
# name = "Rehan" # 2
# def name1(): ## 1,4
#     name = input("Enter your name:==  ") # 5

#     print(f"Your name :>   {name}") # 6
    




# name1() # 3
# print(name) # 7

# def add(n1,n2):

#     print("Adding",n1+n2)

#     # return n1+n2
# z =int(input("Enter your"))
# y =int(input("Enter your"))
# add(z,y)

# def addition(n1):
#     total = 0
#     for i in n1:
#         total = total+i
#     print(total,end=" : ")


# return krane ke liy us variable me us object ko store krna hoga iske bad variable ko print krnana hai


# Examaple

# def addition(n1,n2):
#     total = n1+n2
#     # print(total,end=" : ")
#     return total

# a = addition(2,3)
# print(a)
# print(addition(2,4))

# jaise isme mai return me 2,3 liya or ab use hme return krna hai to uske liy hme addition(2,3) ko x me store krna hai. or usko directly vi print kar skte hai

'''Second Method'''

# def Addition(num1,num2):
#     total = num1 + num2
#     print(total)
#     # return total

# x = Addition(1,3)

# print(x)

'''When use return and print'''

def Addition(num1,num2):#1,6
    total = num1 + num2#7
    print(total)#8
    return total#9
    

x = int(input("Enter a  first number:==  "))#2
y = int(input("Enter a  first number:== "))#3

# d = Addition(x, y) 

def Check(num):#4,11
    if num%2 == 0:#12
        # print("Even")
        return "Even"
    else:
        # print("Odd")
        return "Odd"

# print(Addition(x,y))
d = Addition(x,y)#5   d = ak alias hai
c =Check(d)#10

print(c)

# or
# print(Check(d))
