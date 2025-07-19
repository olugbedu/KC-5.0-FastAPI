movies = {
    "Avengers": {"seats": 10, "price": 1500},
    "Wedding Party": {"seats": 8, "price": 2000},
    "Beekeeper": {"seats": 5, "price": 1000},
    "John Wick": {"seats": 12, "price": 1800}
}

def show_movies():
    print("\n Available Movies ")
    for name, details in movies.items():
        print(f"{name}: {details['seats']} seats left, ₦{details['price']} per ticket")
    print()

def book_ticket():
    movie = input("Enter movie name: ").title()
    if movie not in movies:
        print("Movie not found.\n")
        return
    try:
        qty = int(input("How many tickets? "))
        if qty <= 0:
            print("Quantity must be greater than 0.\n")
            return
        available = movies[movie]["seats"]
        if qty > available:
            print(f"Only {available} seats available.\n")
            return
        movies[movie]["seats"] -= qty
        total_price = qty * movies[movie]["price"]
        print(f"Booked {qty} ticket(s) for {movie}. Total: ₦{total_price}\n")
    except ValueError:
        print("Invalid number of tickets.\n")

def main():
    while True:
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            show_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Thanks for using the booking system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-3.\n")

main()
