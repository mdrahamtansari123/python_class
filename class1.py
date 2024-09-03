# OOPS:  object oriented programming language



# class MyClass:  # MyClass is class name 
#   x = int(input("enter the first number:: === "))
#   z = int(input("enter the first number:: === "))
#   total = x+z

# y = MyClass()## This y is an  Object  
# print(y.total)  ## This is Object v


# class My_saif:
#     x = 12
#     y = 13
#     print(x+y)



# obj1 = My_saif()

# x = 100 # object 

# print(type(x))  # type is object

# x = [1,3,4,5,6,7,8,]
# print(type(x))

# class Employee:
#     x = 34  # attribute
#     y = 54

#     print(x+y)
   

# obj1 = Employee()

# print(obj1)

# class Employee:
#     def __init__(self):  # constracter
#         self.name = "Saif"   # attribute    
#         self.age = 28
#         self.village = "Korwadih" 

# obj1 = Employee()

# print(obj1.__dict__)

# print(obj1.age)

# print(obj1.village)


# parameter constructor

class Employee:
    def __init__(self, name ,age,village ):
        self.name = name 
        self.age = age
        self.village = village


    def school(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My village is {self.village}")

    def Marketing(self):

        print(f"My name is {self.name}, My age is {self.age},  My village is {self.village}")




obj1 = Employee("Saif",23, "Korwadih")

obj2 = Employee("Rahamat", 27,"Koshiyar")
obj3 = Employee("Anjar", 28, "Garhwa")

print(obj1.name)
print(obj1.__dict__)
print(obj1.village)

obj2.age=25

# print(obj2.school())

obj2.school()

obj3.Marketing()

print(obj3.name)










