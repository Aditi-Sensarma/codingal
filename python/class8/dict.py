dict = {
    "key1" : "value1",
    "key1" : "value2",
    "key1" : "value3",
    "key1" : "value4",
    "key1" : "value5",
}

print(dict)
print(dict["key1"])
print(dict["key2"])
print("----------")
for x in dict.keys():
    print(x)

print("--------------")
for y in dict.values():
    print(y)

print("-------------")
for x,y in dict.items():
    print(x,y)