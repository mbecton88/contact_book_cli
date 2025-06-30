# contact_book.py

import json

# --- Constants ---
CONTACTS_FILE = "contacts.json"


# --- Function Definitions ---

def load_from_file():
    """
    Loads contacts from the JSON file.
    Handles FileNotFoundError and JSONDecodeError if the file is missing or empty.
    """
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # File doesn't exist yet, so we start with an empty list.
        return []
    except json.JSONDecodeError:
        # File is empty or corrupted, start with an empty list.
        return []


def save_to_file(contact_book):
    """
    Saves the entire contact book list to the JSON file.
    """
    with open(CONTACTS_FILE, 'w') as file:
        # indent=4 makes the JSON file nicely formatted and readable.
        json.dump(contact_book, file, indent=4)


def display_menu():
    """
    Displays the main menu of the program.
    """
    print("\n--- Contact Book Menu ---")
    print("(1) Add a new contact")
    print("(2) View all contacts")
    print("(3) Exit")
    print("-------------------------")


def add_contact(contacts_list):
    """
    Prompts the user for contact details, creates the new contact,
    and adds the contact to the provided list.
    """
    print("\nAdd a New Contact:")
    contact_name = input("Please enter contact name: ")
    contact_number = input("Please enter contact phone number: ")
    contact_email = input("Please enter contact email address: ")

    # Using the keys from our original plan for consistency.
    new_contact_info = {
        "name": contact_name,
        "phone": contact_number,
        "email": contact_email
    }

    contacts_list.append(new_contact_info)
    print(f"\nContact for '{contact_name}' added successfully!")
    return contacts_list


def view_all_contacts(contact_book):
    """
    Displays all contacts in a user-friendly format.
    """
    print("\n--- All Contacts ---")
    # Handle the edge case where the book is empty.
    if not contact_book:
        print("Your contact book is empty.")
    else:
        # Loop through and print each contact with nice formatting.
        for i, contact in enumerate(contact_book, 1):
            print(f"{i}. Name:  {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print("-" * 20)  # A separator line for readability


def main():
    """
    The main function that runs the application loop.
    """
    # Now, we load the contacts from the file at the very beginning.
    contact_book = load_from_file()

    while True:
        display_menu()
        menu_choice = input("Enter your choice (1-3): ")

        if menu_choice == '1':
            contact_book = add_contact(contact_book)
        elif menu_choice == '2':
            view_all_contacts(contact_book)
        elif menu_choice == '3':
            # We save the contacts right before exiting.
            save_to_file(contact_book)
            print("\nContacts saved. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")


# This is the correct syntax with double underscores.
# This is the only function call needed outside of other functions.
if __name__ == "__main__":
    main()
