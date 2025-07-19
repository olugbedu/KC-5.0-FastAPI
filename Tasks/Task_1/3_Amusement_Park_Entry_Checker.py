print("Welcome to the Amusement Park Entry Checker!\n")

while True:
    name = input("Enter visitor's name (or type 'done' to exit): ")
    if name.lower() == 'done':
        break

    age = int(input("Enter age: "))

    if age < 5:
        price = 0
    elif 5 <= age <= 17:
        price = 5
    elif 18 <= age <= 59:
        price = 10
    else:  # age 60+
        price = 7

    has_coupon = input("Do you have a coupon? (Yes/No): ")
    if has_coupon.lower() == 'yes' and price > 0:
        discount = price * 0.2
        price -= discount
        print(f"Coupon applied! Discount: ${discount:.2f}")

    print(f"{name}'s final ticket price: ${price:.2f}\n")
