# Main script to run the expense tracker

"""
Expense Tracker CLI
-------------------
This script provides a command-line interface for users to:
    - Add a single expense
    - Bulk upload expenses from a CSV file
    - View a summary or analysis of expenses
"""


import sys
import os


# Ensure the expense_tracker folder is in sys.path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
# expense_tracker_dir = os.path.join(parent_dir, "expense_tracker")
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from expense_tracker import services

def print_menu():
    """Display the main menu options to the user."""
    print("\nExpense Tracker Menu:")
    print("1. Add a single expense")
    print("2. Bulk upload expenses from CSV")
    print("3. View summary/analysis")
    print("4. Exit")


def add_single_expense():
    """Prompt user for expense details and add a single expense."""
    date = input("Enter date (YYYY-MM-DD): ").strip()
    amount = input("Enter amount: ").strip()
    category = input("Enter category: ").strip()
    # No description field in model/services
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    try:
        services.add_expense(date=date, amount=amount, category=category)
        print("Expense added successfully.")
    except Exception as e:
        print(f"Failed to add expense: {e}")


def bulk_upload_expenses():
    """Prompt user for CSV file path and upload expenses in bulk."""
    file_path = input("Enter the path to the CSV file: ").strip()
    try:
        expenses = services.bulk_upload_expenses(file_path)
        print(f"Successfully uploaded {len(expenses)} expenses from CSV.")
    except Exception as e:
        print(f"Failed to upload expenses: {e}")


def view_summary():
    """Display a summary or analysis of expenses."""
    try:
        summary = services.get_summary()
        print("\nExpense Summary/Analysis:")
        print(summary)
    except Exception as e:
        print(f"Failed to retrieve summary: {e}")

def main():
    """Main loop for the CLI application."""
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_single_expense()
        elif choice == '2':
            bulk_upload_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
