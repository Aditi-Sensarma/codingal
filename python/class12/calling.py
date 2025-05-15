file = open(r"C:\Users\Aditi Sensarma\OneDrive\Desktop\codingal\python\class12\feedback.txt", 'a+')


name = input("Enter your full name: ")
feedback = input("Enter your experience: ")
rating = input("Enter your rating: ")


dict = {
        "name" : name,
        "feedback" : feedback,
        "rating" : rating
    }


print(dict)

file.write(str(dict) + "\n")
file.seek(0)

for line in file:
    print(line)
    print("----------")

file.close()

