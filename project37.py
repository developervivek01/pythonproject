"""DAY 37 OF 100 DAYS PYTHON PROJECT"""
books = [] 

while True:
    print("\n1.Add  2.View  3.Issue  4.Return  5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        books.append([title, author, True])
        print("Book added!")

    elif choice == "2":
        if len(books) == 0:
            print("No books yet.")
        for i in range(len(books)):
            if books[i][2]:
                status = "Available"
            else:
                status = "Issued"
            print(i + 1, books[i][0], status)

    elif choice == "3" or choice == "4":
        title = input("Title: ")
        found = False
        for book in books:
            if book[0] == title:
                found = True
                if choice == "3" and book[2]:
                    book[2] = False
                    print("Book issued!")
                elif choice == "4" and not book[2]:
                    book[2] = True
                    print("Book returned!")
                else:
                    print("Not possible right now.")
        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice.")