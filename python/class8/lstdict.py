Stdlist = []

for i in range(2):
    list = []
    name = input("Enter your name")
    list.append(name)
    age = input("Enter your age")
    list.append(age)
    grd = input("Enter your grade")
    list.append(grd)
    Stdlist.append(list)

print(Stdlist)

Stddetail = {}

for x in Stdlist:
    name = x[0]
    Stddetail[name] = {"age" : x[1], "grade" : x[2]}

print(Stddetail)
