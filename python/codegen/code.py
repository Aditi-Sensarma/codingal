import qrcode

x = qrcode.QRCode()
print(x)

data = input("Enter data to encode in qrcode: ")

x.add_data(data)
x.make()

img = x.make_image()

filename=input("Enter file name: ")
img.save(filename+".png")