file = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class12\feedback.txt","a+")

file1 = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class12\game.txt","r")

file.seek(0)

x = file.read()

y = file1.read()


file.write(y)
file.seek(0)
content = file.read()

print(content)

