import csv
from datetime import datetime

def validate_expense_data(date, amount, category):
    # Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        return False
    # Validate amount
    try:
        if float(amount) <= 0:
            return False
    except Exception:
        return False
    # Validate category
    if not category or not isinstance(category, str):
        return False
    return True

def parse_csv(csv_file_path):
    rows = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if set(row.keys()) >= {"date", "amount", "category"}:
                rows.append(row)
            else:
                raise ValueError("Malformed CSV file")
    return rows# Helper functions (CSV parsing, etc.)
