print("===== MINI SHOPPING CART =====")

# Product names
products = ["Rice", "Milk", "Soap", "Bread"]

# Product prices
prices = [50, 30, 20, 40]

# Cart list
cart = []
total = 0

while True:
    print("\nAvailable Products:")
    for i in range(len(products)):
        print(i + 1, ".", products[i], "- Rs", prices[i])

    print("5. Exit")

    choice = int(input("Enter product number: "))

    if choice >= 1 and choice <= 4:
        cart.append(products[choice - 1])
        total = total + prices[choice - 1]
        print(products[choice - 1], "added to cart.")

    elif choice == 5:
        break

    else:
        print("Invalid choice!")

# Final Bill
print("\n===== YOUR CART =====")

if len(cart) == 0:
    print("Cart is empty.")
else:
    for item in cart:
        print("-", item)

    print("Total Amount = Rs", total)

print("Thank you for shopping!")