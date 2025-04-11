import turtle
x = turtle.Turtle("turtle")
y = turtle.Screen()
y.bgcolor("white")
x.color("black")

list = ["red","blue","green","orange","yellow","pink","purple","indigo","brown"]
x.speed(10)
for i in range(100):
    x.pencolor(list[i%9])
    x.forward(i*2)
    x.left(144)

turtle.done()

