'''Access Modifiers'''

# Modifi means no change date in with function with variable data only access in class not use other class 

#  1. Private, 2. Procted , 3. Public  no access another class 

# from random import randint

# class Student:

#     def __init__(self) -> None:
#         self.name = input("Enter you name: ")
#         self.__account = randint(1000000,9999999)  ### This is private account __account, __balance
#         self.__balance = 0
#         self.age = 2  ## this is public account
    
    # def displayBalance(self):
    #     print(f"Balance: {self.__balance}")  # this is get method

    # def setBalance(self, Amount):   # Set method
    #     self.__balance = Amount


#     def display(self):
#         print(f"name====", self.name)
#         print(f"account===", self.__account)
#         print(f"balance===", self.__balance)

# obj = Student()

# obj.display()
# obj.__account=1  # this is the changeble account
# print(obj.__account) ## this is a error code no access  this private account     
# obj.display()
# obj.displayBalance()

# obj.setBalance(100)

# obj.age(87)  ## this is a public

# print(obj._Student__account)  ##  this is the changeble account  @ never do this, its says name mangline







# list1 = [100, 200, 300, 400, 500]

# list1.reverse()

# print(list1)

# list2 = list1[::-1]

# print(list2)

'''
Concatenate two lists index-wise
'''

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# list3 = [i+j   for i,j in zip(list1, list2)]

# print(list3)



# '''
# Second Method Concatenate two lists index-wise
# '''
# g =["wh","i","y", "na"]
# h =["at","s","our", "me"]

# k= []

# for i,j in zip(g,h):
#     x = i+j
#     k.append(x)
# print(k)

# ''''
# Exercise 3: Turn every item of a list into its square
# '''

# numbers = [1, 2, 3, 4, 5, 6, 7]
# y = []
# for i in numbers:
#     x = i*i
#     y.append(x)
# print(y)

# ''''
# Exercise 4: Concatenate two lists in the following order'''

# list1 = ["Hello ", "take "]
# list2 = ["Rahamat", "Sir"]

# y = []
# for i in list1:
#     for j in list2:
#         z = i+j
#         y.append(z)
# print(y)

# '''Second Method'''
# res = [x + y for x in list1 for y in list2]
# print(res)

# ''''Exercise 5: Iterate both lists simultaneously'''

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for i, j in zip(list1, list2[::-1]):
    
#     print(i, j)

# '''
# Exercise 6: Remove empty strings from the list of strings
# '''

# mn = ["Age","","Raj","Koshiyar","","","Thin"]

# c = list(filter(None,mn))
# print(c)
    
    
  
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# # print(list1[2][2])

# list1[2][2].append(700)

# print(list1)


# '''
# Exercise 8: Extend nested list by adding the sublist'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

# list1[3].append(sub_list)
# list1[2][1][2].append(sub_list)

# print(list1)

# for i in sub_list:
#     list1[2][1][2].append(i)
# print(list1)



# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3] = 200

# print(list1)

# '''Second Methods'''

# index = list1.index(20)

# list1[index] = 200
# print(list1)

# '''Exercise 10: Remove all occurrences of a specific item from a list.'''

# list1 = [5, 20, 15, 20, 25, 50, 20]

# for i in list1:
#     if i == 20:
#         list1.remove(i)

#         print(list1)

# s = 0
# n = int(input("Enter number "))

# for i in range(1, n + 1, 1):
#     print(i)
#     s += i
#     print(s)
# # print("\n")
# # print("Sum is: ", s)


# numbers = [12, 75, 150, 180, 145, 525, 50]

# for i in numbers:
#     if 



# x = [51,7,10,34,2,8]

# min1 = x[0]

# for i in x:
#     if i < min1:
#         min1 = i

# print(min1)



#  49. Write a Python program to Replace all Characters of a List Except the given character
# y =  ['P', 'Y', 'T', 'H', 'O', 'N']

# p = input("enter character ")
 
# count = 0
# for i in range(0,len(y)):
#     if  y[i] !=p :
#         y[i] = "@" 
        

#     elif y[i] == p and count ==0:

#         count = count + 1

#     else:
#         y[i] = "@"
# print(y)



# change = int(input("enter the row:== "))
# # print(change) #value

# a = [1,2,3,4,5,6,7,8,10,11,12,9]

# y = a[11] #change hoga

# # print(y)
# # d = a[7]
# # print(d)

# for i in range(len(a)):
#     if a[i] == change:
#         # a[i+1]  = y
#         a.insert(i+1,y)
#         # a.remove(y)
# print(a)

# print(13/3)


#3. Write a Python program to get the largest number from a list Sample Output

# m = [1,7,10,34,2,8,87,8,765]

# l1 = m[0]
# print(l1)

# for i in m:
#     print(i)

#     if i > l1:
#         l1 = i
# print(l1)

# 4. Write a Python program to get the smallest number from a list Sample Output

# y = [51,7,10,34,2,8]

# d = y[0]

# for i in y:
#     if i < d:
#         d = i
# print(d)

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings Sample Output

x = ['abc', 'xyz', 'aba', '1221','36553']

for i in x:
    if  i[0] == i[-1]:
        print(i)
