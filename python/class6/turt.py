import turtle 
x = turtle.Turtle("turtle")
y = turtle.Screen()
y.setup(500, 500)
y.bgcolor("purple")
x.color("white")

for i in range(4):
    x.forward(100)
    x.right(90)
turtle.done()