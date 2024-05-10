 # 5 types of Data in python

# 1. Integer :=   1,2,3,4,5,66,7,8,9,9,10,11,12,13,........



# v = +3
# print(type(v))

# '''2.  Float:=   1.3, 2.4, 3.5'''
# x = +7.6
# print(type(x))

# # 3. complex:= 3+2j, 8+2j, 9+2j

# c = -1+6j
# print(type(c))

# d = 3j-7j+8j-6j
# print(type(d))

# # 4.  String:= "Saif",'Ali'

# name = 'saif'

# print(type(name))

# y = '''Saif'''
# print(type(y))

# x = str("Hello World")
# y = "Hello i am saif ali \n and i'm from jharkhand and \n my education and \n qualification BCA from SSJSN college garhwwa"
# print(y)

# # 5. Boolean:= True, False
# b = False
# print(type(b))

# # 6. None := None
# b = None

# print(type(b))

# f = str(54) # mutable
# print(type(f))

# c = int("Rahamat") # immutable
# print(type(c))



# name = "Hello World gi"

# # print(len(name))
# print(name[6:2])

# c = 2,3,4,6,8

# print(c[2])

# x = [1,2,3,4,5]

# y = [3,4,4,5,6,7,8]

# z = set(x) | set(y)

# print(z) 


#Python Arithmetic Operators
# x = 12
# y = 3

# print(x+y) # 15 Addition

# print(x-y) # 9  subtraction

# print(x*y) # 36 Multiplication

# print(x/y) # 4.0 division

# print(x//y) #  floor division

# print(x%y) # Modulus
# print(x**y) # Exponentiation

# h = 17

# g = 5

# print(h/g) # remainder value in output

# Write a Python program to remove duplicates from a list

# Sample Output

# x = [1,2,3,7,2,1,5,6,4,8,5,4]

# y = set(x)

# print(list(y))

# a = 13
# b = 3

# print(a//b) # remainder value in output


'''2.        Assignment Operators'''

# x = 5
# x **= 12



# print(x)

'''3 Python Comparison Operators '''

# x = 12
# y = 23

# print(x<y) # True

# print(x!=y) # False
# print(x>=y)
# print(x<=y)
# print(x==y)


'''4. Python Logical Operators '''

# and 
# y = 4
#  2
# 6

# y = 4
#       # Triue  and True = True
# print(y>2 and y<6) 

# x = 67
# y = 8

# print(x>y or x>y)

# x = int(input("saif number print kijiy   "))
# y = str(input("Rahamat number print kijiy   "))
# print(x,y)

# x = 11
# y = 4
# print(x/y)
# print(x|y)

'''6 Identity Operators '''
# x = 10
# y = 11
# print(id(x))
# z = x
# print(id(y))
# print(id(z))

# z = x is y
# print(z)
# x = 'Saif'
# y = 'Saif'
# print(id(x))
# print(id(y))
# z = x is y 
# print(z)

# x = [1,2,3,4]
# y = [1,2,3,4]
# print(id(x))
# print(id(y))

# print(x is y)
# a = None
# b = None
# print(id(a))
# print(id(b))
# print(a is b)

# x = 12
# y = 13
# print(id(x))
# print(id(y))

# print(x is not y)

# a = [1, 2, 3, 4,5]
# b = [1, 2, 3, 4, 5]
# c = a
# d = b

# Comparing and printing return values
# print(a is  b)
# print(a is c)
# print(b is d)
# print(a is not b)

'''6. Membership Operators'''
x = 24
y = 20


# list = [10, 20, 30, 40, 50]
 
# if (x not in list):
#     print("x is NOT present in given list")
# else:
#     print("x is  present in given list")
 
# if (y in list):
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")

# fruits = ["apple", "banana", "cherry"]

# if "banana" in fruits:
#     print("Yes, banana is a fruit!")
# # using "not in" operator
# if "orange" not in fruits:
#     print("Yes, orange is not in the list of fruits")

'''7.  Bitwise Operators:== binary'''


# AND :== &
# OR :== |
# XOR :== ^

# x = 10
# print(bin(x))
# y = 765
# print(bin(y))


# print(x | y)

# x = 10
# y = 8
# z = 2

# print(bin(x))
# print(bin(y))

# print(x and y)
# print(x or y)
# print(x ^ y)

# print(bin(z))


''' Python If ... Else'''
# if
# if elif
# if else
# single line if else
# 
# a = 93
# b = 34

# if a>b:
#     print("a is greater than b")

# x = 34
# y = 304

# if x>y:
#     print("x is greater than y")
# elif x<y:
#     print("x is lesser than y")
# else:
#     print("x is equal to y")

# a = 12   #1. a is equal b and not equal b  # 2 b less than a 



# if a == b:
#     print("a eqal to  b") # True

# else:
#     print("a  equal not  b") # false

# if a%2:
#     print("a is odd")
# else:
#     print("a is even")

# 1. write a python script to check whether a given number is positive or non positive.
# 2. write a python script to check whether a given number is division by 5 or not?
# 3. write a python script to check whether a given number is even or odd?

# 4. write a python script to print greater between two number print number only once if both the number are same ?.

# x = int(input("Enter a number:  "))
# print(x)

# if x > 0:
#     print(" is positive")
# elif x == 0:
#     print(" is zero")
# else:
#     print(" is negative")

# x = input("Enter your username:  ")
# y = input("Enter your password: ")

# if x == "saif123" and y == "1234":
#     print("Login Successfull")
# else:
#     print("Login Failed")

 # start : Step

# lowrd
# b = "Helloworld"
# # print(b[2::1])
# print(b[7:])
# print(b[-4::1])
# # print(b[2:2:10])

# year = int(input("Enterv your no."))

# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# else:
#     print("{0} is not a leap year".format(year))

# user_input_month = input("Enter a month")

# if user_input_month in ("January","March","May","July","August","October","December"):
#     print("This is month of 31 ")

# for i in range(1,4):    
# #     for j in range(1,4):
# #         print(i)

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# for letter in 'geeksforgeeks':

#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)



# i = 1
# while i < 6:
#   print(i)
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   if i == 4:
#     break
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# saif 5 bar 

# i = 1
# while i < 6:
#     print("Saif")
#     i += 1

# i = 11
# while i > 0:
#     i -= 1
#     print(i, end=',')

# str1 = "a2b3c4"

# obj1 = ''

# for i in str1:
#     if i.isalpha():
#         var = i
#     else:
#         num = int(i)
#         obj1 = obj1+(var*num)

# print(obj1)












 




