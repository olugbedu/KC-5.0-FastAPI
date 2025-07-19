from datetime import datetime
from diary_tools import save_entries, load_entries

# DiaryEntry class
class DiaryEntry:
    def __init__(self, title, content, date=None):
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M")
        self.title = title
        self.content = content

# Diary system class
class Diary:
    def __init__(self):
        self.entries = []
        self.load()

    def add_entry(self):
        title = input("Title: ").strip()
        if not title:
            print("Title cannot be empty.\n")
            return
        content = input("Content:\n").strip()
        if not content:
            print("Content cannot be empty.\n")
            return
        entry = DiaryEntry(title, content)
        self.entries.append(entry)
        print("Entry added.\n")

    def view_all(self):
        if not self.entries:
            print("No entries found.\n")
            return
        print("\n--- All Diary Entries ---")
        for i, e in enumerate(self.entries, 1):
            print(f"{i}. [{e.date}] {e.title}")
            print(f"   {e.content}\n")

    def search_entries(self):
        keyword = input("Enter date or title keyword to search: ").lower()
        found = False
        for e in self.entries:
            if keyword in e.date.lower() or keyword in e.title.lower():
                print(f"\n[{e.date}] {e.title}")
                print(e.content)
                print()
                found = True
        if not found:
            print("No matching entries found.\n")

    def save(self):
        save_entries(self.entries)
        print("Diary saved. Goodbye!")

    def load(self):
        data = load_entries()
        for item in data:
            entry = DiaryEntry(item["title"], item["content"], item["date"])
            self.entries.append(entry)

# Menu
def main():
    diary = Diary()

    while True:
        print("1. Add Entry")
        print("2. View All Entries")
        print("3. Search by Date/Title")
        print("4. Save & Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            diary.add_entry()
        elif choice == "2":
            diary.view_all()
        elif choice == "3":
            diary.search_entries()
        elif choice == "4":
            diary.save()
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
