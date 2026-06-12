# Command-Line Contact Book Application

CONTACTS_FILE = "contacts.txt"


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("Contact added successfully!\n")


def view_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("No contacts found.\n")
                return

            print("\n--- Contact List ---")
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name}")
                print(f"Phone: {phone}")
                print(f"Email: {email}")
                print("-" * 25)

    except FileNotFoundError:
        print("No contact file found.\n")


def search_contact():
    search_name = input("Enter name to search: ").lower()

    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = file.readlines()

            found = False

            for contact in contacts:
                name, phone, email = contact.strip().split(",")

                if search_name in name.lower():
                    print("\nContact Found:")
                    print(f"Name: {name}")
                    print(f"Phone: {phone}")
                    print(f"Email: {email}")
                    print("-" * 25)
                    found = True

            if not found:
                print("Contact not found.\n")

    except FileNotFoundError:
        print("No contact file found.\n")


def menu():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    menu()
