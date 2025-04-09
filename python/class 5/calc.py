def add(a,b):
    print(f"{a} + {b} = {a+b}")

def sub(a,b):
    print(f"{a} - {b} = {a-b}")

def mul(a,b):
    print(f"{a} x {b} = {a*b} ")

def div(a,b):
    if a>b:
           print(f"{a} ÷ {b} = {a/b}")
    else:
         print(f"{b} ÷ {a} = {b/a}")

while True : 
     print("1. Addition")
     print("2. Subtraction")
     print("3. Multiplication")
     print("4. Division")
     print("5. Exit")

     ch = int(input("Enter your choice : "))
     if ch == 1:
          num1 = int(input("Enter the first number : "))
          num2 = int(input("Enter the second number : "))
          add(num1,num2)
     elif ch ==2:
           num1 = int(input("Enter the first number : "))
           num2 = int(input("Enter the second number : "))
           sub(num1,num2)
     elif ch == 3:
           num1 = int(input("Enter the first number : "))
           num2 = int(input("Enter the second number : "))
           mul(num1,num2)
     elif ch == 4:
           num1 = int(input("Enter the first number : "))
           num2 = int(input("Enter the second number : "))
           div(num1,num2)
     else:
          break
        

    
      

