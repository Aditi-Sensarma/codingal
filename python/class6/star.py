import turtle
x = turtle.Turtle("turtle")
y = turtle.Screen()
y.bgcolor("white")
x.color("black")

list = ["violet","indigo","blue","green","yellow","orange","red"]
x.speed(0)
for i in range(100):
    x.pencolor(list[i%9])
    x.circle(i)
    x.left(59)
    

turtle.done()

