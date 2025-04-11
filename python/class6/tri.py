import turtle
x = turtle.Turtle("turtle")
y = turtle.Screen()
y.bgcolor("blue")
x.color("white")

for i in range(3):
    x.forward(50)
    x.left(120)

turtle.done()