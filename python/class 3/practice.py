num = int(input("Enter a number : "))

if num <0 :
    print("It is a negative number")
elif num ==0 :
    print("It is 0")
elif num > 0 and num<10 :
    print("It is less than 10")
elif num >10 and num<20 :
    print("It is between 10 and 20")
else : 
    print("Greater than 20")
