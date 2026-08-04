"""DAY 18 of 100days 
python project"""
balance = 960000
amount = int(input("ENTER WITHDRAW AMOUNT:"))

if amount <= balance:
    balance -= amount
    print("WITHDRAW SUCCESFULL")
    print("Remaining Balance",balance)
else:
    print("INSUFFIENT BALANCE ")    