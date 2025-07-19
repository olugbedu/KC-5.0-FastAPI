from billing import Cart, load_bills

def main():
    cart = Cart()

    while True:
        print("1. Add Product to Cart")
        print("2. View Cart and Total")
        print("3. Save Bill to File")
        print("4. View Previous Transactions")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Product name: ")
            price = input("Product price: ")
            quantity = input("Quantity: ")
            cart.add_product(name, price, quantity)

        elif choice == "2":
            cart.view_cart()

        elif choice == "3":
            cart.save_bill()

        elif choice == "4":
            bills = load_bills()
            if not bills:
                print("No previous transactions found.\n")
                continue
            for i, bill in enumerate(bills, 1):
                print(f"\nTransaction {i} - {bill['timestamp']}")
                for item in bill['items']:
                    print(f"  {item['name']} - ₦{item['price']} x {item['quantity']} = ₦{item['total']}")
                print(f"  Total: ₦{bill['total']}")
            print()

        elif choice == "5":
            print("Exiting... Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please select 1–5.\n")

if __name__ == "__main__":
    main()
