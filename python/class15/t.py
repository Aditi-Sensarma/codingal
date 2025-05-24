from tkinter import *
win = Tk()

win.title("First window app")
win.geometry("500x500")

text = Label(win,text="Welcome to my first App")
text.pack()

inputArea = Entry(win)
inputArea.pack(padx=10,pady=20)


inputArea2 = Entry(win)
inputArea2.pack(padx=10,pady=20)



def Add():
    x =int(inputArea.get())
    y =int(inputArea2.get())
    print(x+y)
   
Button2 = Button(win,text="Addition", command=Add)

Button2.pack(padx=10,pady=20)

def Sub():
    x =int(inputArea.get())
    y =int(inputArea2.get())
    print(x-y)
   
Button1 = Button(win,text="Subtraction", command=Sub)

Button1.pack()


def Mul():
    x =int(inputArea.get())
    y =int(inputArea2.get())
    print(x*y)
   
Button3 = Button(win,text="Multiplication", command=Mul)

Button3.pack(padx=10,pady=20)

def Div():
    x =int(inputArea.get())
    y =int(inputArea2.get())
    print(x/y)
   
Button4 = Button(win,text="Division", command=Div)

Button4.pack()




win.mainloop()