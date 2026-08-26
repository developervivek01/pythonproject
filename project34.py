import time 

while True:
    current_time = time.strftime("%H:%M:%S")
    print(f"\r{current_time}",end="") 

    time.sleep(1)
