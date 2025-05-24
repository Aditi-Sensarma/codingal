file = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class13\Codingal.txt","r")


x = file.read()

file.seek(0)

lineNum=0
for line in file :
    print(line)
    lineNum +=1
    if lineNum ==4:
        break
    print("---------------")