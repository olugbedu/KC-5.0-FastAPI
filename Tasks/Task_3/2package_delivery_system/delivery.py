import uuid
from delivery_utils import save_packages, load_packages

class Package:
    def __init__(self, sender, recipient, status="Pending", id=None):
        self.id = str(id) if id else str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.status = status

class DeliverySystem:
    def __init__(self):
        self.packages = []
        self.load()

    def register_package(self):
        sender = input("Enter sender name: ")
        recipient = input("Enter recipient name: ")
        package = Package(sender, recipient)
        self.packages.append(package)
        print(f"Package registered! ID: {package.id}\n")

    def mark_delivered(self):
        pkg_id = input("Enter package ID to mark as delivered: ")
        for pkg in self.packages:
            if pkg.id == pkg_id:
                if pkg.status == "Delivered":
                    print("Package is already marked as delivered.\n")
                else:
                    pkg.status = "Delivered"
                    print("Package marked as delivered.\n")
                return
        print("Package not found.\n")

    def view_packages(self):
        if not self.packages:
            print("No packages found.\n")
            return
        print("\n--- All Packages ---")
        for i, pkg in enumerate(self.packages, start=1):
            print(f"{i}. ID: {pkg.id}")
            print(f"   From: {pkg.sender} | To: {pkg.recipient} | Status: {pkg.status}")
        print()

    def save(self):
        save_packages(self.packages)
        print("Packages saved.\n")

    def load(self):
        data = load_packages()
        for item in data:
            pkg = Package(
                sender=item["sender"],
                recipient=item["recipient"],
                status=item["status"],
                id=item["id"]
            )
            self.packages.append(pkg)

def main():
    system = DeliverySystem()

    while True:
        print("1. Register Package")
        print("2. Mark Package as Delivered")
        print("3. View All Packages")
        print("4. Save & Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            system.register_package()
        elif choice == "2":
            system.mark_delivered()
        elif choice == "3":
            system.view_packages()
        elif choice == "4":
            system.save()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
