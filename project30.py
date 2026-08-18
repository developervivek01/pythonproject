contacts = []

while True:
    print("1.ADD CONTACT")
    print("2.VIEW CONTACT")
    print("3.SEARCH CONTACT")
    print("4.DELETE CONTACT")
    print("5.EXIT")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contact = {"name": name, "number": number}
        contacts.append(contact)
        print("Contact saved!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            for i in range(len(contacts)):
                print(i + 1, contacts[i]["name"],contacts[i]["number"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c["name"].lower() == search_name.lower():
                print(c["name"], "-", c["number"])
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        num = int(input("Enter contact number (position) to delete: "))
        if num > 0 and num <= len(contacts):
            removed = contacts.pop(num - 1)
            print("Deleted:", removed["name"])
        else:
            print("Invalid selection.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")