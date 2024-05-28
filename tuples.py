# 2 Tuples 

# tuples := () parenthesis
# tuple is a sequence
# tuple is class 
# tuple is iterable
# tuple is immutable (change ham nhi kar sakte hain data type ko)
# tuple may contain differrent types of values
# tuple elements are index:

# How to tuple object:==

# print(type(t1 := (10,20,30,40,50,60)))

# t1 = (10,20,30,40,50,60,40,30)
# print(type(t1))
# print(t1[1])

# print(t1)

# s1 = {1,2,3,1,2,3}

# print(s1)

# t2 = 10,20,30,40,50,60,40,30
# print(type(t2))

# a,b,c,d = t2 # unpacking 
# print(type(a))



# t3 = 'a','b','c','d'
# print(t3)


# slicing
# t2 = (10,0,30,40,50,60,20,70)
# v = list(t2)
# print(v)
# print(t2[::-1])

# t3 = (1,2,3)

# for loop me print kijiy
# for i in t2:
#     print(i,end=',')

# print(t2+t3)
# print((t3)*3)

# print(t2>t3)

# t2 = (10,0,30,40,50,60,20,70,20)
# print(t2.count(20))
# print(max(t2))
# print(min(t2))
# print(t2.index(20))

# b = t2.append(100)

# print(len(t2))



t2 = (10, 0, 30, 40, 50, 60, 20, 70, 20)

# 100

# Convert the tuple to a list
t2_list = list(t2)
t2_list.append(100)
t2_list.append("Saif")
t2_list.insert(0, 567)


# print(t2_list)

# Append data
# t2.index[1] = "Saif"

# Convert the list back to a tuple
t2_updated = tuple(t2_list)
print(t2_updated)








