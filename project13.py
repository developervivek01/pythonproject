'''DAY 13 OF 100DAYS 
PYTHON PROJECT'''
import random
items = ["rock","paper","scissor"]

computer = random.choice(items)
user = input("rock paper and scissor").lower()
print("computer choose",computer)

if user == computer:
    print("match draw")
elif user == "rock" and computer =="scissor":
    print("user winn !!")    
elif user == "paper" and computer =="rock":
    print("computer winn !!")    
elif user == "scissor" and computer =="paper":
    print("user winn !!")    
else:
    print("computerwin")  
    