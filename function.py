# Functios notes:

# What is namespace 
# a1 = 10
# a2 = 20
# a3 = 30
# a4 = 40
# print(id(a1), id(a2), id(a3))

# types of namespace
#1. Built-in namespace:= Built-in namespace jb kam krta hai tb hm python interpreter start karte hai Exmaple:= dir()
#2. Module-level/global namespace := ye yesa module namespace hota hai jo module ko import krne ka kam karte hai

# Example:== example.py

# def example():
    #print("This is example")

# display.py

# def display():
#   print("display")

# mai.py

# import example, display
# print(example.display())

#3. Local namespace:=   ye namespace function or classes ke liy hota hai

# Example:== 
# a=50
# def func1():
#     a = 10
#     def func3():
#         b = 20
#         print(dir())
#     print(dir())
#     func3()
# def func2():
#     a = 20

# print(dir())
# func1()


# #4. Enclosed namespace

# # Video
# # LEGB = Local , Enclosed , Global, Builtin

# # 1. Example
# x = 100  # global variable
# def outer():
#     global x
#     x = x+20
#     print(x)
#     x = 20  # local variable
#     print(x)

# outer()

# # 2. Example

# x = 100
# def outer():
#     x = 0 # Non Local variable

#     def inner():
#         nonlocal x
        
#         x = x+200  # Non Local variable ya Enclosed variable
#         print(x)

#         x = 20 # locals  variable
#         print(x)
#     inner()

# outer()

## 3 video

# How function Work

# def outer():
#     x = 100
#     print("Hello World")
#     def inner():
#         print("This is inner")

#     inner()
# outer()

# Aliasing function

# def outer():
#     x = 100
#     print("Hello World")
#     def inner():
#         print("This is inner")

#     inner()
# new = outer  # this alias function
# new()
# outer()

# Closures in python function

# def outer():
#     def inner():
#         x = 200
#         return x
#     return inner()
# print(outer())

# def outer():
#     x = 900
#     print(x)
#     def inner():
#         x = 200
#         return x
#     return inner
# new = outer()
# print(new())

## video 4

# Decorator for video

# def decor(outer):
#     def inner():
#         x = outer()
#         print("Decorator for video")
#         return x
#     return inner
        

# @decor
# def outer():
#     print("This outer")
   
    
# decor = outer()
# print(decor)

def shout(text): 
    return text.lower() 

def whisper(text):
    
    return text.upper()

print(whisper('hello')) 
print(shout('HELLO')) 

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting)
def student(name):
    student = name(input("Enter Your Student Name :=  "))
    print (student)
    # return  student

greet(shout)
greet(whisper) 
student(whisper)



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

# def addition(num1,num2): # this parameters
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
# jb koi returns krat hai use variable me save krte hai then print krte hai ya fir directly print kra skte hai

## jab koi variable dega use return krna pdega or use return karne ke liy ak object ko varialble me store krna hoga

# Example

# def add1(num1,num2):
#      total = num1+num2
#      return total
#     #  print(total)
# # add1(23,45) ##This is no print

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

# def Addition(num1,num2):#1,6
#     total = num1 + num2#7
#     print(total)#8
#     return total#9
    

# x = int(input("Enter a  first number:==  "))#2
# y = int(input("Enter a  first number:== "))#3

# d = Addition(x, y) 

# def Check(num):#4,11
#     if num%2 == 0:#12
#         # print("Even")
#         return "Even"
#     else:
#         # print("Odd")
#         return "Odd"

# # print(Addition(x,y))
# d = Addition(x,y)#5   d = ak alias hai
# c =Check(d)#10

# print(c)

# or
# print(Check(d))


# def student():
#     first_name = input("Eneter your first name: =")
#     last_name = input("Eneter your last name: =")
#     # print(first_name, last_name)
#     return first_name, last_name

# x = student()
# print(x)



## sub ,add,mul

# def sum2(num1, num2):
#     total = num1+num2
#     return total

# def sub(num1, num2):
#     total = num1-num2
#     return total

# def mul(num1, num2):
#     total = num1*num2
#     return total

# def cheak(total):
#     if total%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
        
# num1 = int(input("Enter the number first number: == "))
# num2 = int(input("Enter the number first number: == "))

# x = sum2(num1, num2)
# y = mul(num1, num2)
# z = sub(num1, num2)

# print(x)
# print(y)
# print(z)

# cheak(x)
# cheak(y)
# cheak(z)


# fonction code

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Dictionary mapping operation names to functions
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# Example usage
a = 10
b = 5
operation = "multiply"
result = operations[operation](a, b)
print(result)  # Output: 50



def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(func, value):
    return func(value)

# Applying functions
print(apply_function(square, 3))  # Output: 9
print(apply_function(cube, 3))    # Output: 27

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

# Storing functions in a list
func_list = [greet, farewell]

# Calling functions from the list
for func in func_list:
    print(func("Dave"))
# Output:
# Hello, Dave!
# Goodbye, Dave!