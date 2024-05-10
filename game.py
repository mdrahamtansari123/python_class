# # import tkinter as tk
# # import random

# # # Define the uppercase and lowercase letter pairs
# # letter_pairs = {
# #     'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
# #     'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
# #     'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
# #     'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
# #     'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y',
# #     'Z': 'z'
# # }

# # # Create a dictionary to store the letter coordinates
# # letter_coordinates = {}

# # # Function to generate random coordinates for the letters
# # def generate_random_coordinates():
# #     return random.randint(50, 300), random.randint(50, 300)

# # def start_game():
# #     canvas.delete("all")
# #     letter_coordinates.clear()
    
# #     # Create and display the lowercase and uppercase letters at random positions
# #     for letter in letter_pairs.keys():
# #         lowercase_x, lowercase_y = generate_random_coordinates()
# #         uppercase_x, uppercase_y = generate_random_coordinates()
        
# #         # Display lowercase letter
# #         canvas.create_text(lowercase_x, lowercase_y, text=letter_pairs[letter], font=("Arial", 24))
        
# #         # Display uppercase letter
# #         canvas.create_text(uppercase_x, uppercase_y, text=letter, font=("Arial", 24))
        
# #         # Store the coordinates
# #         letter_coordinates[letter] = (lowercase_x, lowercase_y), (uppercase_x, uppercase_y)

# # def check_answer():
# #     for letter, (lowercase_coord, uppercase_coord) in letter_coordinates.items():
# #         if canvas.coords(letter)[0] == lowercase_coord[0] and canvas.coords(letter)[1] == lowercase_coord[1]:
# #             if canvas.coords(letter)[2] == uppercase_coord[0] and canvas.coords(letter)[3] == uppercase_coord[1]:
# #                 continue
# #         return False
# #     return True

# # # Function to handle mouse dragging
# # def on_drag(event):
# #     x, y = event.x, event.y
# #     canvas.move(tk.CURRENT, x - canvas.coords(tk.CURRENT)[0], y - canvas.coords(tk.CURRENT)[1])

# # def on_release(event):
# #     if check_answer():
# #         status_label.config(text="Correct! You matched all letters.")
# #     else:
# #         status_label.config(text="Try again. Not all letters are matched.")

# # # Create the main window
# # root = tk.Tk()
# # root.title("Match Lowercase to Uppercase Game")

# # # Create GUI elements
# # canvas = tk.Canvas(root, width=400, height=400)
# # status_label = tk.Label(root, text="Drag the lowercase letters to match them with uppercase letters.", font=("Arial", 12))

# # # Place GUI elements on the window
# # canvas.pack(pady=20)
# # status_label.pack(pady=10)

# # # Start the game
# # start_game()

# # # Bind mouse events
# # canvas.bind("<ButtonRelease-1>", on_release)
# # canvas.bind("<B1-Motion>", on_drag)

# # # Run the main loop
# # root.mainloop()

# import tkinter as tk

# # Define the uppercase and lowercase letter pairs to match
# letter_pairs = {
#     'A': 'a',
#     'B': 'b',
#     # Add more pairs as needed
# }

# class MatchGame(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Match Uppercase to Lowercase Game")
#         self.geometry("400x300")

#         self.canvas = tk.Canvas(self, width=400, height=200)
#         self.canvas.pack(pady=20)

#         self.status_label = tk.Label(self, text="Drag the uppercase letters to match them with lowercase letters.", font=("Arial", 12))
#         self.status_label.pack(pady=10)

#         # Create and display the letters
#         self.letters = {}  # To store letter widgets
#         for uppercase, lowercase in letter_pairs.items():
#             self.create_letter(uppercase, 50, 100, "uppercase")
#             self.create_letter(lowercase, 250, 100, "lowercase")

#     def create_letter(self, letter, x, y, letter_type):
#         # Create a letter as a label
#         label = tk.Label(self.canvas, text=letter, font=("Arial", 24), bg="lightgray", relief=tk.RAISED)
#         label.bind("<ButtonPress-1>", self.on_click)
#         label.bind("<B1-Motion>", self.on_drag)
#         label.bind("<ButtonRelease-1>", self.on_release)
#         label.place(x=x, y=y, anchor=tk.CENTER)

#         # Store the letter and its type (uppercase/lowercase)
#         self.letters[letter] = {
#             "label": label,
#             "type": letter_type,
#             "original_position": (x, y),
#         }

#     def on_click(self, event):
#         self.active_letter = event.widget

#     def on_drag(self, event):
#         x, y = event.x_root - self.winfo_x(), event.y_root - self.winfo_y()
#         self.active_letter.place(x=x, y=y, anchor=tk.CENTER)

#     def on_release(self, event):
#         if self.active_letter:
#             active_letter_text = self.active_letter.cget("text")
#             active_letter_type = self.letters[active_letter_text]["type"]
#             active_letter_x, active_letter_y = self.active_letter.winfo_x(), self.active_letter.winfo_y()

#             for letter, info in self.letters.items():
#                 if letter != active_letter_text and info["type"] != active_letter_type:
#                     letter_x, letter_y = info["original_position"]

#                     if active_letter_x - 30 < letter_x < active_letter_x + 30 and \
#                             active_letter_y - 30 < letter_y < active_letter_y + 30:
#                         self.active_letter.place(x=letter_x, y=letter_y, anchor=tk.CENTER)
#                         break
#             else:
#                 self.active_letter.place(x=self.letters[active_letter_text]["original_position"][0],
#                                          y=self.letters[active_letter_text]["original_position"][1],
#                                          anchor=tk.CENTER)

#             self.active_letter = None

#         if self.check_win():
#             self.status_label.config(text="Congratulations! You matched all the letters.")

#     def check_win(self):
#         for uppercase, lowercase in letter_pairs.items():
#             uppercase_coords = self.letters[uppercase]["label"].winfo_geometry().split('+')[1:3]
#             lowercase_coords = self.letters[lowercase]["label"].winfo_geometry().split('+')[1:3]

#             if abs(int(uppercase_coords[0]) - int(lowercase_coords[0])) > 30 or \
#                     abs(int(uppercase_coords[1]) - int(lowercase_coords[1])) > 30:
#                 return False

#         return True


# if __name__ == "__main__":
#     app = MatchGame()
#     app.mainloop()


# def func(x=1, y=2):
#     x = x+y
#     y += 1
#     print(x,y)

# func(y=2,x=1)

# list1 = [1,2,['Rahamat','a'], 5,6,[9,[67,'Ajay'],"Ashis"]]
# print(list1[5][2][-1:-4])
# print(list1[5][2][0::-3])
# print(list1[5][2][5:1:-1])
# sih
# Lst = [50, 70, 30, 20, 90, 10, 50]
 
# Display list

# print(Lst[::3])

# print(Lst[::-2])

# for i in Lst:
#     if i%3 !=0:
#         print("divisible")
#     else:
#         print("not")

# List = ['Geeks',8, 4, 'geeks !']
 

# print(List[:1:2])


# list1=[10,20,30,30,40,50]
# for i in list1:
#     if i == 30:
#         list1.remove(i)
# print(list1)

# list3 = ["Hello World"]

# print(list3[0][::-1])

# number = [1,2,3,4,5,6,7,8,9,10,3,4,1]

# for x in number:
#     y=0
#     while y>x: 
#         if x%y==0:
#             y+=1
#         else:
#             y+=1
#     if y==2:
#         print(x)
    
x=10
y=2
count=0
for a in range(2,x):
    if a%y==0:
        count=count+1
        y=y+1
if count==2:
    print(a)
count=0





# list2 =["SS", "Dambaruu"]

# result = [i for i in list2 if len(i)>6]
# print(*result)

# print(len(list2))


# for i in list2:
#     if len(i) > 6:
#         print

# class x:
#     def __init__(self):
#         self.__num1 =5
#         self.num2 = 2

#     def display_values(self):
#         print(self.__num1,self.num2)
# class y(x):
#     def __init__(self):
#         super().__init__()
#         self.__num1=1
#         self.num2 = 6
# obj = y()
# obj.display_values()


# import time

# a = time.time()
# print(a)


# func = lambda a,b:(a**b)
# print(func(float(10),16))


# tinylist = [753001,'dambaruu']
# print(tinylist*2)

# s1 ={ 1,2,3,4,5}
# s2 ={2,4,6}
# print(s1^s2)


# a= [1,2,3,4]
# b= [3,4,5,6]
# c= [x for x in a if x not in b]
# print(c)

# x = [[0],[1]]
# print(''.join(list(map(str,x)),))

# list2 = [1,0,2]
# a,b,c = list2[::-1]
# print(list2[c])

# check = lambda num :  num%2==0

# x = int(input("Please Enter Your Number"))

# if check(x):
#     print("True")
# else:
#     print("False")

# number = lambda num : [i for i in range(1,num+1)]

# l1 = int(input("Enetr a number"))

# print(number(l1))

# if l1%2 == 0:
#     print("Even Number")

# else:
#     print("Odd Number")

# check = lambda num : print("Even") if num%2 == 0 else print("Odd")

# check(1)

import datetime
import time


current_time = datetime.datetime.now()
expiry_time = current_time + datetime.timedelta(minutes=2)


print(current_time)
print(expiry_time)

