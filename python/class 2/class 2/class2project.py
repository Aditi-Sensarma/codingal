x = int(input("Enter a number : "))
y = int(input("Enter another number : "))
z = int(input("Enter one last number : "))

x1 = x
x = y
y = z
z = x1

print("After swapping: ")
print(f"First number {x}, second number {y} and third number {z}")