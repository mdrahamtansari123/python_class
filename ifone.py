#1.   Python Conditions and If statements

# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)
# str1 = "dambaruu"
# print (str1[1:3:1])

# Select the correct ways to get the value of marks key.

# def sum1(num1, num2):
#     total = num1+num2
#     print(total)
#     return total

# x = sum1(1,2)
# print(x,end=" ")

# def check(total):
#     if total % 2==0:
#         print("Even num")
#     else:
#         print("odd num")
# check(x) 


def addition_list(number):
    total = 0
    for i in number:
        if i % 3 == 0:
          total = total + i
    print(total)
    return total
    
my_list = [1,2,3,4,5,6,7,8,9]
x = addition_list(my_list)


def mult(num):
   x = num*2
   print(x)
   return x
   
x = mult(x)

def discount(num):
   num = num*100 - 50
   print(num)
   return num
  
discount(x)







