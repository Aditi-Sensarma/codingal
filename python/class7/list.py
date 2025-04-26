ages = [10,20,30,40,50]

print(ages)
print(ages[0])
print(ages[-5])


print(ages)
x = int(input("Enter a number : "))
ages.append(x)
print(ages)
ages.pop()
print (ages)

index = int(input("Enter index : "))
ages.pop(index)
print(ages)