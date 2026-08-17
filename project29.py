import time

print("Speed Typing Test !!!")

sentance = "abcdefghijklmnopqrstuvwxyz"
print("\n Type This Exactly...")
print(sentance)

input("\n Press Enter To start....")

start = time.time()

typed = input("\nStart Typing...:")

end=time.time()

time_taken = round(end-start,2)

speed = round(len(sentance)/time_taken,2)

print("Time Taken : " ,time_taken,"second")
print("Typing Speed",speed,"letters/sec")




