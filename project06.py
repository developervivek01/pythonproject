"""day 06 of 100days python project"""
a1 = int(input("enter no1:"))
a2 = int(input("enter no2:"))
a3 = int(input("enter no3:"))
a4 = int(input("enter no4:"))

if (a1>a2 and a1>a3 and a1>a4):
    print("a1 is greatest",)
elif (a2>a1 and a2>a3 and a2>a4):
    print("a2 is greatest",)
elif (a3>a2 and a3>a1 and a3>a4):
    print("a3 is greatest",)
elif (a4>a2 and a4>a3 and a4>a1):
    print("a4 is greatest",)
