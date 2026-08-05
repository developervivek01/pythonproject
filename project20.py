"""DAY 20 OF 100DAYS 
PYTHON PROJECT"""
import qrcode

data = input("ENTER TEXT OR LINK :")

img = qrcode.make(data)

img.save("img.png")

img.show()

print("QRCODE GENRATED !!!")