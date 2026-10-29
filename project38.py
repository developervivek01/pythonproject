"""DAY 38 OF 100 DAYS PYTHON PROJECT - Simple Notepad"""

import os

# all notes are saved in this folder
folder = "notes"
if not os.path.exists(folder):
    os.mkdir(folder)

while True:
    print("\n1.New 2.View 3.Add 4.List 5.Del 6.Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Note name: ")
        print("Type note. Write 'save' to finish.")
        lines = []
        while True:
            line = input()
            if line == "save":
                break
            lines.append(line)
        file = open(folder + "/" + name + ".txt", "w")
        file.write("\n".join(lines) + "\n")
        file.close()
        print("Note saved!")

    elif choice == "2":
        name = input("Note name: ")
        path = folder + "/" + name + ".txt"
        if os.path.exists(path):
            file = open(path, "r")
            print("\n--- " + name + " ---")
            print(file.read())
            file.close()
        else:
            print("Note not found.")

    elif choice == "3":
        name = input("Note name: ")
        path = folder + "/" + name + ".txt"
        if os.path.exists(path):
            text = input("Add text: ")
            file = open(path, "a")
            file.write(text + "\n")
            file.close()
            print("Text added!")
        else:
            print("Note not found.")

    elif choice == "4":
        files = os.listdir(folder)
        if len(files) == 0:
            print("No notes yet.")
        for i in range(len(files)):
            print(i + 1, files[i].replace(".txt", ""))

    elif choice == "5":
        name = input("Note name: ")
        path = folder + "/" + name + ".txt"
        if os.path.exists(path):
            os.remove(path)
            print("Note deleted!")
        else:
            print("Note not found.")

    elif choice == "6":
        print("Bye!")
        break

    else:
        print("Invalid choice.")