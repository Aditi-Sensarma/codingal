file = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class12\game.txt","a+")


UserName = input("Enter your Username: ")
level = input("Enter your level: ")
score = input("Enter your score: ")


dict = {
        "UserName" : UserName,
        "level" : level,
        "score" : score
    }


print(dict)

file.write(str(dict) + "\n")
file.seek(0)

for line in file:
    print(line)
    print("----------")

file.close()

