tasks = []

while True:
    print("\n MY TO DO LIST")
    print("1.ADD TASK")
    print("2.VIEW TASK")
    print("3.REMOVE TASK")
    print("4.exit")

    choice = input("choose option  :")

    if choice=="1":
        task = input("Enter task")
        tasks.append(task)
        print("TASK ADDED !!!")

    elif choice == "2":
        print("\n YOUR TASK !")
        for i ,task in enumerate(tasks,start=1):
          print(f"{i},{task}")

    elif choice==3:
        task = input("enter task")
        if task in tasks:
            task.remove(task)
            print("task removed")
        else:
            print("task not found ") 
    elif choice=="4":
        print("bye")

    else:
        print("invaid choice ")               


            


    


