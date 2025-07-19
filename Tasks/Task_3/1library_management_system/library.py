from library_utils import save_books, load_books

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []
        self.load()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        self.books.append(Book(title, author))
        print(f"Book '{title}' added.\n")

    def borrow_book(self):
        title = input("Enter book title to borrow: ")
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You borrowed '{book.title}'.\n")
                return
        print("Book not available or not found.\n")

    def return_book(self):
        title = input("Enter book title to return: ")
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You returned '{book.title}'.\n")
                return
        print("Book not found or already returned.\n")

    def view_books(self):
        if not self.books:
            print("No books in library.\n")
            return
        print("\n--- Library Books ---")
        for i, book in enumerate(self.books, 1):
            status = "Available" if book.available else "Borrowed"
            print(f"{i}. {book.title} by {book.author} - {status}")
        print()

    def save(self):
        save_books(self.books)
        print("Library saved. Goodbye!")

    def load(self):
        book_data = load_books()
        for item in book_data:
            book = Book(item["title"], item["author"], item["available"])
            self.books.append(book)

def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Save & Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.borrow_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            library.view_books()
        elif choice == "5":
            library.save()
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
