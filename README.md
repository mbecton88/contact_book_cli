# 📞 Contact Book CLI Application

## 🚀 Overview

This is a simple command-line interface (CLI) application designed to help you manage your contacts efficiently. Whether you need to add a new contact, view existing ones, update details, or remove entries, this tool provides a straightforward interface to keep your contact information organized.

It's built with Python, focusing on simplicity and ease of use for everyday contact management.

## ✨ Features

* **Add New Contacts:** Easily add names, phone numbers, and email addresses.
* **View Contacts:** Display all stored contacts in a clear, readable format.
* **Update Contacts:** Modify details for existing contacts.
* **Delete Contacts:** Remove unwanted contact entries.
* **Persistent Storage:** Your contacts are saved to a `contacts.json` file, ensuring your data is retained even after closing the application.

## 🛠️ Installation & Setup

To get this application up and running on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/mbecton88/contact_book_cli.git](https://github.com/mbecton88/contact_book_cli.git)
    cd contact_book_cli
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 How to Run

Once setup, you can launch the application:

```bash
python main.py


🖥️ Usage
Upon running main.py, you'll be greeted with a menu of options:

Welcome to your Contact Book!
Please choose an option:
1. Add a new contact
2. View all contacts
3. Update a contact
4. Delete a contact
5. Exit
Enter your choice:
Follow the on-screen prompts to interact with your contact book.

💡 Lessons Learned & Challenges Faced
Developing this CLI application presented a few interesting challenges and learning opportunities:

Input Validation Robustness: Ensuring robust user input validation was crucial. Initially, handling non-numeric input for choices or incorrectly formatted data (e.g., non-integers when an integer was expected) required careful attention to avoid crashes. I learned the importance of using try-except blocks and str.isdigit() more effectively. A specific instance was understanding why user_input == 0 (string vs. int) failed when user_input.isdigit() was already true, leading to a deeper understanding of type checking and conversion.

Persistent Data Storage (JSON): Implementing persistent storage using JSON was a key learning curve. Understanding how to correctly read from and write to contacts.json while maintaining data integrity (e.g., handling empty files, corrupted data, or concurrent writes if this were a multi-user app) was vital. The process involved ensuring proper serialization and deserialization.

Git Tracking Issues (.gitignore and git rm --cached): I encountered a specific challenge with Git where contacts.json was briefly tracked but then needed to be untracked and ignored. This led to confusion around git rm --cached failing because the file was already untracked after deletion, and the importance of adding it to .gitignore before initial staging to prevent accidental commits. It reinforced the understanding of git status output and the difference between "untracked" and "tracked but deleted."

Refactoring for Readability: As the application grew, refactoring functions (e.g., the initial days_to_units example) to improve modularity and readability became increasingly important. It highlighted the value of breaking down complex tasks into smaller, manageable functions.

🤝 Contributing
Contributions are welcome! If you have suggestions for features, bug reports, or want to improve the code, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature X').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details. (If you have a https://www.google.com/search?q=LICENSE file, link it here. If not, consider adding one!)
