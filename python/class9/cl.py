class Human:
    def  __init__(self,nValue,aValue,hValue,wValue):
        name = nValue
        age = aValue
        height = hValue
        weight = wValue
        print("Constructor of human is called, one human is created")
        print("name is ", self.name, "age is ", self.age, "height is ", self.height,"weight is", self.weight)
    def eat(self):
        print(self.name,"is eating")

akash = Human("akash kumar roy", 20, 170, 65)
aditi = Human("aditi ", 14, 170, 45)

print("name of akash is", akash.name,"height of akash is",akash.height,"age of akash is",akash.age)
print("name of aditi is", aditi.name,"height of aditi is", aditi.height,"age of aditi is",aditi.age)


aditi.eat()
akash.eat()