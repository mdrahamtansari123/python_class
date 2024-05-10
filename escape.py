#  \' single quite
#  \" Double quite
# \\ Backslash print('rahamatK\\oshiyar')
# \n new line print('Rahamat \nansari\njharkhand')
# \t tab  print('Rahamat \tbishrampur\tjharkhand')
# \b backspace

# print('Rahamat \tbishrampur\tjharkhand')
# print('rahamat K\\oshiyar')
# name = 'Rajsfdf'
# print(f"{name}mohit")

# print("Annu ra\bdha")
# print('Rahamat \nansari\njharkhand')

# b = [1,2,3,4,5,6,7,8,9,10,11,12]

# b[4] = 7
# print((b[::-1]))

# print('rahamatK\\oshiyar')

# for x in range(1,6):
#     # for y in range(1,6):
#     #     print(x,end='')

#     print(x)/

# for x in range(1,6):
#     for y in range(1,6):
#         for z in range(1,6):
#             print(y,end='')
#         print()
    # print()

# for x in range(5,0,-1):
#     for y in range(5,0,-1):
#         print(y, end='')
#     print()

# n = 5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print((x*y),end="")
#     print()


# n = 5

# p = 1

# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print(p, end=' ')
#         p +=2
#     print()
# n = 5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print((x*y), end=' ')
        
#     print()


# for x in range(1,6):
#     for y in range(1,4):
#         print(x,y, end=' ')
        
#     print()

# for x in range(1,6):
#     for y in range(1,4):
#         print(y,x, end=' ')
        
#     print()


# n = 5
# p = 1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(p, end=' ')
#         p += n
#     print()

# n = 5
# p = 1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(p, end=' ')
#         p += n
#     print()
# n = 5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print((x+y)%2,end='')
#     print()
# y = "Raja"
# x = str(f"""Hello{y}""")
# print(type(len(x)))


#Python program to interchange first and last elements in a list

def swip(x):
    a = len(x) # 5
    print(a)
    b = x[0] # print 4
    print(b)
    x[0] = x[a-1]#print 9
    print((x[0]))
    x[a-1]=b # 4
    print(x[a-1], end=' ')
    
    return x


x = [4,5,7,8,8,9]
print(swip(x))

#2.  #Swap Two Elements in a List using comma assignment 



# def swipPosition(list,pos1,pos2):
#     list[pos1],list[pos2] = list[pos2],list[pos1]

#     return list

# list = [2,4,6,7,8,9]  # pos1 = 1, 2 pos2 = 3, 6
#                     # out_put = [6,4,2,7,8,9]
# pos1,pos2 = 1,3
# print(swipPosition(list,pos1-1,pos2-1))



# def y(list,pos1,pos2):
#     list[pos1],list[pos2] = list[pos2],list[pos1]
#     return list

# list = [1,2,3,4,5,6,6,7,8]

# pos1 ,pos2 = 1,9

# print(y(list,pos1-1,pos2-1))

# This is factorial no.

# def y(number):
#     if (number==0 or number==1):
#         return 1
#     else:
#         return number * y(number-1)
# print(y(8))

# for x in range(1, 6):
#     for j in range(1,6):
#         print((x+j)%2, end=' ')
#     print()

# for x in range(1, 6):
#     for j in range(0,6):
#         print((x+j)%2, end=' ')
#     print()

# for x in range(0, 6):
#     for j in range(1,6):
#         print((x%j)%2, end=' ')
#     print()

# for x in range(1, 6):
#     for j in range(0,6):
#         print((x%2), end=' ')
#     print()

# for x in range(1, 6):
#     for j in range(0,6):
#         print((j%2), end=' ')
#     print()

