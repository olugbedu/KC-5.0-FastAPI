customers_served = 0

while True:
    name = input("\nEnter customer name (or type 'exit' to quit): ")
    if name.lower() == 'exit':
        break

    burgers = int(input("Number of burgers ($5 each): "))
    fries = int(input("Number of fries ($2 each): "))
    drinks = int(input("Number of drinks ($1.5 each): "))

    total = (burgers * 5) + (fries * 2) + (drinks * 1.5)

    if total > 20:
        discount = total * 0.10
        total -= discount
        print(f"Discount applied: ${discount:.2f}")

    print(f"\n{name}'s Bill:")
    print(f"  Burgers: ${burgers * 5:.2f}")
    print(f"  Fries:   ${fries * 2:.2f}")
    print(f"  Drinks:  ${drinks * 1.5:.2f}")
    print(f"  Total:   ${total:.2f}")

    customers_served += 1

print(f"\nTotal customers served: {customers_served}")
