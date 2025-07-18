# Data models (Expense, etc.)
# Data models (Expense, etc.)

class Expense:
    def __init__(self, date: str, amount: float, category: str):
        self.date = date
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"Expense(date={self.date!r}, amount={self.amount!r}, category={self.category!r})"