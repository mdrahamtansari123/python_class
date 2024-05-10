#LEGB = Local , Enclosed, Global, Build-in  verible



## 1.  
x = 100 # Global verible
def outer():
    global x  # Global verible
    x = x+20
    print(x)  # Print is Built in name 
    x = 23  # Local veriable
    print(x)  #Print is Built in name

outer()



''' 2.  Non - Local veriable '''

x = 100 # Global verible
def outer():
    x = 20 # Non - Local veriable and i can say that Enclosed of Non Local veriable

    def inner():
        nonlocal x
        x = x  + 200 # Local veriable
        print("This is 2 Question Answer  Nolocal Veriable :>>> ",x)  # Print is Built in name 
       
    inner()  

outer()
    