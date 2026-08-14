# Mini ATM System

account = {
    "name": "Rahul",
    "pin": "1234",
    "balance": 5000
}

print("===== MINI ATM =====")

pin = input("Enter your PIN: ")

if pin == account["pin"]:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", account["balance"])

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                account["balance"] = account["balance"] + amount
                print("Money deposited successfully.")
                print("New balance:", account["balance"])
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")

            elif amount > account["balance"]:
                print("Insufficient balance.")

            else:
                account["balance"] = account["balance"] - amount
                print("Please collect your cash.")
                print("Remaining balance:", account["balance"])

        elif choice == "4":
            print("\nAccount Name:", account["name"])
            print("Account Balance:", account["balance"])

        elif choice == "5":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN.")
    print("Access denied.")