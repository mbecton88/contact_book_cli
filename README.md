Command-Line Contact Book
A simple, persistent command-line contact book application built with Python. This project allows users to add, view, and manage their contacts directly from the terminal. All contacts are saved to a local contacts.json file, ensuring data persists between sessions.

Features
This application provides a user-friendly menu to perform the following actions:

Current Features (MVP)
Add a new contact: Save a contact's name, phone number, and email address.

View all contacts: Display a clean, numbered list of all saved contacts.

Persistent Storage: Automatically loads contacts from contacts.json on startup and saves any changes on exit.

Future Features (Planned)
Search for a specific contact by name.

Update an existing contact's details.

Delete a contact from the book.

Prevent duplicate contact names.

Requirements
Python 3.6 or newer

Setup and Installation
To get this project running locally, follow these steps:

Clone the repository:

git clone https://github.com/mbecton88/contact_book_cli.git
cd contact-book-cli

Create and activate a virtual environment:

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

No external libraries are required for the MVP, so no installation is necessary.

Usage
Once the setup is complete, you can run the application with the following command:

python contact_book.py

You will be greeted with a menu where you can choose to add or view contacts. To exit the application and save your contacts, simply choose the "Exit" option from the menu.
