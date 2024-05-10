# What is ist
# []
# List is a class
# List is a sequence
# list is a iterable
# list elements are index
# list is growble and shrinkable
# list can store more than one element
# list can stotre Hetrogeneous elements

# Exmple



l2 = [ ]

l3 = ["Korwadih", "Garhwa", "Kalyanpur", "Chiniyan"]

l4 = [10,"Saif",3+4j,True,7.8]

# for i in l4:
#     print(i,end='')

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# How to access the list elements?
# for i in l1:
#     if i % 2 == 0:
        
#         print("Even number")
#     else:
        
#         print("Odd number")

# List object [index]

# mul = 1

# for i in l1:
#     mul = mul * i
#     print(mul)

# h2 = l1[2]
# print(h2)

# How to edit the list Element 

# l1[2] = "100"
# print(l1)

# Concepts of indexing:= 

# How to add more values to the list?

# list1 = [1, 2, 3, 4, 5]

# list object.append(value)
# list object.insert(value)
# list1.append(6)
# print(list1)
# list1.append(7)
# print(list1)

# list1.insert(-1, "Saif")
# print(list1)

# list1.pop(3)
# print(list1)
# list1.pop(2)
# print(list1)
# list1.remove(2)
# print(list1)

list1 = [1, 6, 2, 3, 5, 4,6,6]

# print(sum(list1))
# print(max(list1))
# print(min(list1))
# print(len(list1))

# print(sorted(list1))

# print(list1.count(6))

# list1 = [1, 6, 2, 3, 5, 4,] # Korwadih

# list2 = [1, 2, 3, 4] # kalyanpur

# list1.extend(list2)

# print(list1)

# a,b,c,d = list1

# for i in a:
#     print(i)

# print(list1+list2)

# print(list1-list2)

# print(list1*4)

# list2 = [1, 2, 3, 4,5,]

# for i in list2:
#     print(i,end=',')


# for i in list2:
#     if i > 5:
#         print(i,end=',')
# list2 = [1, 2, 3, 4,5,]
# list2.reverse()
# print(list2) 

# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "Apple"]

# newlist = []

# for x in fruits:
#     if "a" in x.lower():  
#         newlist.append(x)

# print(newlist)

# # second method 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango", "Apple"]
# newlist = []

# for x in fruits:
#     if "A" in x or "a" in x:  
#         newlist.append(x)  

# print(newlist)

# 1. Create a string variable named `my_string` with the value "Hello, Python!".
# print(my_string := "Hello, Python")

# 2. Print the third character of `my_string`.

# print(my_string[2])

# 3. Use slicing to print the substring "Python" from `my_string`

# print(my_string[6:13])

# 4. Concatenate `my_string` with another string " Welcome to the world of programming!" andprint the result.

# print(result := my_string + " Welcome to the world of programming!")


# 5. Format the following variables into a string: name = "Alice", age = 30, country ="USA". The output should be "Alice is 30 years old and lives in USA".

# name = "Alice"
# age = 30
# country ="USA"

# print(f"{name} is {age} years old and lives in {country}")

# 6. Create a string with multiple occurrences of a character, such as "aaabbbccc". Count and print the number of occurrences of the character 'b'

# my_string = "aaabbbccc"
# count_b = my_string.count('b')

# print("Number of occurrences of 'b':", count_b)

# 7. Convert the string "HELLO" to lowercase using a string method.
# name = "HELLO"

# x = name.lower()
# print(x)

# 8. Write a program that takes a sentence as input and counts the number of vowels (a, e, i, o, u) in the sentence.

# sentence = input("Enter a sentence: ")

# vowels = 'aeiouAEIOU'
# count = 0

# for i in sentence:
#     if i in vowels:
#         count += 1
#         print("number of vowels: = ",i)

# 9. Use string interpolation to create a formatted string that includes variables `x = 10` and `y = 20`. The output should be "The value of x is 10 and y is 20".

# x = 10
# y = 20

# print(f"The value of x is {x} and y is {y}")

# # 10. Reverse the string "python" using slicing.
# name = 'python'

# 12. Replace all occurrences of 'a' with 'e' in the string "banana" and print the modified string.

# x = name[::-1]
# print(x)

# 11. Write a program that takes a sentence and a word as input and checks if the word is present in the sentence.

# a = [1, 2, 3, 7, 2, 1, 5, 6, 4, 8, 5, 4]


# unique_list = []


# for item in a:
   
#     if item not in unique_list:
#         unique_list.append(item)

# print("List after removing duplicates:", unique_list)



a = 'aabcccaaabccc'

obj1 = ''
#output = a2b1c3a3b1c3

for i in a:
    if i not in obj1:
        obj1 = obj1 + i + str(a.count(i))

print(obj1)



