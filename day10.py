'''DAY 10 OF 100DAYS OF
PYTHON PROJECTS'''
import random
chars = "!@#$%^&*abcdefghi1234567890gh"

password = ""
for i in range(8):
    password+=random.choice(chars)
print("GENRATEDPASSWORD IS :",password)    