num = int(input("Enter a number whose multiplication table you need : "))
print(f"Multiplication table of{num}:")

for i in range (1,11):
    print(num,"x",i,"=",(num * i ))