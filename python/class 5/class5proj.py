num = int(input("Enter a number: "))
x = 0

while num > 0:
    num = int(num / 10 )
    x =+ 1

print(f"The number of digits in the number is: {x}")
