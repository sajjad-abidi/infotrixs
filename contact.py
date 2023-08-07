import os
import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)


def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")


def search_contact(contacts):
    search_term = input("Enter the name to search: ")

    for name, details in contacts.items():
        if search_term.lower() in name.lower():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ")

    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"{name_to_delete} has been deleted.")
    else:
        print(f"{name_to_delete} not found in contacts.")


def update_contact(contacts):
    name_to_update = input("Enter the name of the contact to update: ")

    if name_to_update in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")

        contacts[name_to_update] = {"phone": phone, "email": email}
        print("Contact updated successfully!")
    else:
        print(f"{name_to_update} not found in contacts.")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
