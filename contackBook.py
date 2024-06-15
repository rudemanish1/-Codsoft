class Contact:
    def _init_(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contacts(self, search_term):
        found = False
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                found = True
        if not found:
            print("No matching contacts found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                print(f"Current Details:")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print("Enter new details (leave blank to keep current):")
                new_name = input("New Name: ").strip() or contact.name
                new_phone_number = input("New Phone Number: ").strip() or contact.phone_number
                new_email = input("New Email: ").strip() or contact.email
                new_address = input("New Address: ").strip() or contact.address

                # Update contact details
                contact.name = new_name
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully.")
                return
        print("No matching contacts found.")

    def delete_contact(self, search_term):
        for i, contact in enumerate(self.contacts):
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("No matching contacts found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contacts(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()