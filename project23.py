"""DAY 23 OF 100DAYS PYTHON PROJECT"""
import random

lower = "abcdefghijklmnopqrstyvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "{}[]._.!@#$"

all = lower+upper+numbers+symbols

length = 16
password = "".join(random.sample(all,length))
print(password)