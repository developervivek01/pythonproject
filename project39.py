"""DAY 39 - Password Generator + Checker"""

import random
import string

while True:
    print("\n1.Generate 2.Check 3.Exit")
    choice = input("Choose: ")

    # ---- make a password ----
    if choice == "1":
        size = int(input("Length: "))

        # all letters + numbers + symbols
        chars = string.ascii_letters
        chars = chars + string.digits
        chars = chars + string.punctuation

        password = ""
        for i in range(size):
            letter = random.choice(chars)
            password = password + letter

        print("Password:", password)

    # ---- check a password ----
    elif choice == "2":
        password = input("Enter password: ")
        score = 0

        # point 1: long enough
        if len(password) >= 8:
            score = score + 1

        # point 2: has a number
        for ch in password:
            if ch in string.digits:
                score = score + 1
                break

        # point 3: has a capital letter
        for ch in password:
            if ch in string.ascii_uppercase:
                score = score + 1
                break

        # point 4: has a symbol
        for ch in password:
            if ch in string.punctuation:
                score = score + 1
                break

        print("Score:", score, "/ 4")

        if score == 4:
            print("STRONG")
        elif score == 3:
            print("MEDIUM")
        else:
            print("WEAK")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Wrong choice")