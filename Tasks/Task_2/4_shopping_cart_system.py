store_items = {
    "Rice": 2000,
    "Beans": 800,
    "Oil": 500,
    "Bread": 1500,
    "Milk": 500
}

cart = []

def show_items():
    print("\n Store Items ")
    for item, price in store_items.items():
        print(f"{item}: ₦{price}")
    print()

def add_to_cart():
    item = input("Enter item name to add: ").title()
    if item not in store_items:
        print("Item not available.\n")
        return
    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Quantity must be greater than 0.\n")
            return
        cart.append({"item": item, "quantity": qty, "price": store_items[item]})
        print(f"{qty} x {item} added to cart.\n")
    except ValueError:
        print("Invalid quantity.\n")

def view_cart():
    if not cart:
        print("Cart is empty.\n")
        return
    print("\n Your Cart ")
    total = 0
    for i, entry in enumerate(cart, start=1):
        item_total = entry["quantity"] * entry["price"]
        total += item_total
        print(f"{i}. {entry['item']} x {entry['quantity']} = ₦{item_total}")
    print(f"Total: ₦{total}\n")

def remove_item():
    name = input("Enter item name to remove: ").title()
    for i, entry in enumerate(cart):
        if entry["item"] == name:
            del cart[i]
            print(f"{name} removed from cart.\n")
            return
    print("Item not found in cart.\n")

def clear_cart():
    cart.clear()
    print("Cart cleared.\n")

def main():
    while True:
        print("1. View Store Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Clear Cart")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            clear_cart()
        elif choice == "6":
            print("Thank you for shopping. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.\n")

main()
