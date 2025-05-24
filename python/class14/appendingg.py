file = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class14\f1.txt","a+")
file1 = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class14\f2.txt","r")

file.seek(0)


x = file.read()
y = file1.read()

for line in x:
    print(line)
    print("-------------------------")

