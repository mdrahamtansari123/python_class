# from random import randint

# class Bank:

#     def __init__(self):
#         self.account = randint(100000,999999)
#         self.full_name = input("Enter your name:===    ")
#         self.phone_number = int(input("Enter your phone number:===  "))
#         self.balance = 0

#     def show_balance(self):
#         print(f"Account_Information : {self.full_name}")
#         print(f"Account_Information : {self.account}")
#         print(f"Phone_Information : {self.phone_number}")
#         print(f"Total_Amount : {self.balance}\n")

#     def deposit(self):
#         amount = int(input("Enter your amount"))
#         self.balance = self.balance + amount


#     def withdraw(self):
#         amount = int(input("Enter your amount"))
#         if amount > self.balance:
#             print("Insufficient balance")
            
#         else:
#             self.balance -= amount


# banks = []

# def check_amount_exists(acco_n:int):
#     global banks
#     for bank in banks:
#         if acco_n == bank.account:
#             return bank
#     else:
#         return None




# while True:
#     print("1. Create Account:== ")
#     print("2. Show all Bank Deatils :== ")
#     print("3. Deposit Ammount :== ")
#     print("4. Withdraw  Ammount :== ")
#     print("5. Transfer  Ammount :== ")
#     print("6. Exit :== ")
#     choice = int(input("Enter your choice:=="))

#     if choice == 1:  ###Logic, This is Oprn Account ###
#         obj = Bank()
#         banks.append(obj)
#         print(banks)

#     elif choice == 2:  ###Logic  This is Show Money ###
#             if len(banks) == 0:
#                 print("No Account  Open")

#             else:
#                 for bank in banks:
#                     bank.show_balance()
#     elif choice ==3:  ###Logic,  This is Deposit Money ###
#         if len(banks) == 0:
#             print("No Account  Open")
            
#         else:
#             acco_n = int(input("Enter Your Bank Number in Deposit:== "))
#             for bank in banks:
#                 if acco_n == bank.account:
#                     bank.deposit()
#                     print(f"Amount Deposited : {bank.amount}")
#                     print(f"Balance : {bank.balance}")
#                     break
#                 else:
#                     print("Invalid Account Number")


#     elif choice ==4:  ###Logic, This is Withdraw Money ###
#         if len(banks) == 0:
#             print("No Account  Open")
            
#         else:
#             acco_n = int(input("Enter Your Bank Number Withdraw:==  "))
#             for bank in banks:
#                 if acco_n == bank.account:
#                     bank.withdraw()
#                     print(f"Amount Withdrawn : {bank.amount}")
#                     print(f"Balance : {bank.balance}")
#                     break
#                 else:
#                     print("Invalid Account Number")
                    
#     elif choice ==5:  ### Logic,  This is Transfer Money ###
#         from_acco_n = int(input("Enter Your Amount from which you want to transfer money:==  "))
#         to_acco_n = int(input("Enter Your Amount from which you want to transfer money"))

#         from_acco_n = check_amount_exists(from_acco_n)
#         to_acco_n = check_amount_exists(to_acco_n)
        
#         if from_acco_n != None and to_acco_n != None:  ## from_acco_n means some in object
#             transfer_amount = int(input("Enter your amount from which you want to transfer:==  "))
#             if transfer_amount > from_acco_n.balance:
#                 print("Insufficient balance")
#             else:
#                 from_acco_n.balance -= transfer_amount
#                 to_acco_n.balance += transfer_amount
#                 print(f"Amount Transferred : {transfer_amount}")
#                 print(f"From Account Balance : {from_acco_n.balance}")
#                 print(f"To Account Balance : {to_acco_n.balance}")    
#         else: 
        
#             print("Account Does Not Exist")
#     elif choice ==6:  ### Logic,  This is Exit ###
#         break
            
#     else:
#         print("Invalid choice")




## 2.   parametrise ###
        
# class Student:
#     def __init__(self):
#         self.name = input("Enter your name:===    ")
#         self.age = int(input("Enter your age:===  "))

#     def show_info(self):
#         print(f"Student_Information : {self.name}")
#         print(f"Student_Information : {self.age}")
    
#     def change_name(self,): #new_name:str
#         self.name = input("Change Name")

    


# s1 = Student()

# s1.show_info()
# s1.change_name()

# s1.show_info()

'''   Module  '''  # in Module all definitions function

# def circle(reduse:float):
#     area = 3.14 * reduse * reduse

#     print(f"Area of circle: {reduse} {area}")

# def rectangle(breath:float, length:float):
#     area = length * breath

#     print(f"Area of rectangle:  {area}")

# def trangle(base:float, height:float):
#     area = 0.5 * height * base

#     print(f"Area of trangle:  {area}")
   
# circle(5.4)

# rectangle(4, 6)

### accurance Use 
# my_list = [1,2,2,3,3,3,4,4,4,4,]

# accurance = {x : my_list.count(x) for x in my_list}

# print(f"This is Accurance number{accurance}")

# ''' Split USE '''

# s = "Python is a powerfull programming language"

# word_count = len(s.split())

# print(word_count)

## Encapsulation


class Car:
    def __init__(self) -> None:
        print("Car INT")
        self.color = input("Enetr Is van color")
        self.type = input("Enetr Your type of van")
        self.milage = float(input("Enetr your milage"))
        self.set_capacity = int(input("Enetr set capicity"))

    def show_info(self):
        print(f"Car_Information : {self.color}")
        print(f"Car_Information : {self.type}")
        print(f"Car_Information : {self.milage}")
        print(f"Car_Information : {self.set_capacity}\n")

class Audi(Car):
    def __init__(self) -> None:  #  when run code then print show child class
        print("Audi INT")
        
    # def __init__(self):
    #     super(). __init__()
    #     print("AUDI INT")       # Super function when run code then print show Parent Class
    def set_info_audi(self):
        super().__init__()
        self.electric = input("Enetr Is electric")
        self.city = input("Enetr Your city")

    def audio_info(self):
        self.electric = self.electric
        self.city = self.city

c1 = Audi()
c1.set_info_audi()
c1.show_info()
c1.audio_info()
