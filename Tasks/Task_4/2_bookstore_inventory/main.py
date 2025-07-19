from inventory import add_book, load_books, save_books

def view_books():
    books = load_books()
    if not books:
        print("Inventory is empty.")
        return
    for book in books:
        print(f"\nTitle: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Price: ₦{book['price']}")
        print(f"Stock: {book['stock']}")

def search_books():
    query = input("Search by title or author: ").lower()
    books = load_books()
    results = [book for book in books if query in book['title'].lower() or query in book['author'].lower()]
    if results:
        print(f"\nFound {len(results)} book(s):")
        for book in results:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Price: ₦{book['price']}")
            print(f"Stock: {book['stock']}")
    else:
        print("No matching books found.")

def main():
    while True:
        print("\n=== Bookstore Inventory System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
