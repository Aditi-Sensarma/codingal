class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def info(self):
        print("Width:", self.width, "Height:", self.height)

    def area(self):
        print("Area:", self.width * self.height)

    def perimeter(self):
        print("Perimeter:", 2 * (self.width + self.height))


w = int(input("Enter the width"))
h = int(input("Enter the height"))

r1 = Rect(w,h)



r1.info()
r1.area()
r1.perimeter()

print()

