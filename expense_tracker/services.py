from .models import Expense
from . import utils

# In-memory store for expenses (for summary/analysis)
_expenses_store = []

def add_expense(date: str, amount: float, category: str) -> Expense:
    # Validate input
    if not utils.validate_expense_data(date, amount, category):
        raise ValueError("Invalid expense data")
    expense = Expense(date, amount, category)
    _expenses_store.append(expense)
    return expense

def bulk_upload_expenses(csv_file_path: str) -> list:
    expenses = []
    try:
        rows = utils.parse_csv(csv_file_path)
    except Exception:
        raise ValueError("Malformed CSV file")
    for row in rows:
        try:
            date = row["date"]
            amount = float(row["amount"])
            category = row["category"]
            if utils.validate_expense_data(date, amount, category):
                expense = Expense(date, amount, category)
                expenses.append(expense)
                _expenses_store.append(expense)  # <-- Add this line
        except Exception:
            continue  # Skip invalid rows
    if not expenses and rows:
        raise ValueError("No valid expenses found in file")
    return expenses

def get_summary():
    """
    Returns a simple summary/analysis of all expenses.
    """
    if not _expenses_store:
        return "No expenses recorded yet."
    total = sum(exp.amount for exp in _expenses_store)
    by_category = {}
    for exp in _expenses_store:
        by_category.setdefault(exp.category, 0)
        by_category[exp.category] += exp.amount
    summary_lines = [
        f"Total expenses: {total:.2f}",
        "Expenses by category:"
    ]
    for cat, amt in by_category.items():
        summary_lines.append(f"  {cat}: {amt:.2f}")
    return "\n".join(summary_lines)