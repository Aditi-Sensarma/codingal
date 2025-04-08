num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    isItPrime = True 
    for i in range(2, num): 
        if num % i == 0:  
            print("Not a prime number")
            isItPrime = False  
            break  
    if isItPrime:  
        print("Prime number")
