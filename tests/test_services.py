# Unit and integration tests for services
import pytest
from expense_tracker.models import Expense
from expense_tracker import services

def test_add_single_expense():
    # Test adding a valid single expense
    date = "2024-06-01"
    expense = 25.50
    category = "Food"
    result = services.add_expense(date, expense, category)
    assert isinstance(result, Expense)
    assert result.date == date
    assert result.amount == expense
    assert result.category == category

def test_add_expense_invalid_data():
    # Test adding an expense with invalid data (e.g., negative amount)
    date = "2024-06-01"
    expense = -10.00  # Invalid negative amount
    category = "Food"
    with pytest.raises(ValueError):
        services.add_expense(date, expense, category)

def test_bulk_upload_expenses_valid_csv(tmp_path):
    # Test bulk upload with a valid CSV file
    csv_content = "date,amount,category\n2024-06-01,10.00,Food\n2024-06-02,20.50,Transport\n"
    csv_file = tmp_path / "expenses.csv"
    csv_file.write_text(csv_content)

    results = services.bulk_upload_expenses(str(csv_file))
    assert isinstance(results, list)
    assert len(results) == 2
    assert all(isinstance(exp, Expense) for exp in results)
    assert results[0].date == "2024-06-01"
    assert results[0].amount == 10.00
    assert results[0].category == "Food"
    assert results[1].date == "2024-06-02"
    assert results[1].amount == 20.50
    assert results[1].category == "Transport"

def test_bulk_upload_expenses_invalid_csv(tmp_path):
    # Test bulk upload with an invalid/malformed CSV file
    csv_content = "date,amount,category\n2024-06-01,notanumber,Food\n2024-06-02,20.50\n"
    csv_file = tmp_path / "invalid_expenses.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError):
        services.bulk_upload_expenses(str(csv_file))

def test_bulk_upload_expenses_partial_failure(tmp_path):
    # Test bulk upload where some rows are invalid
    csv_content = (
        "date,amount,category\n"
        "2024-06-01,10.00,Food\n"
        "2024-06-02,-5.00,Transport\n"  # Invalid negative amount
        "2024-06-03,15.00,Utilities\n"
        "2024-06-04,notanumber,Shopping\n"  # Invalid amount
    )
    csv_file = tmp_path / "partial_invalid_expenses.csv"
    csv_file.write_text(csv_content)

    results = services.bulk_upload_expenses(str(csv_file))
    # Expect only the valid rows to be processed
    assert isinstance(results, list)
    assert len(results) == 2
    assert all(isinstance(exp, Expense) for exp in results)
    assert results[0].date == "2024-06-01"
    assert results[0].amount == 10.00
    assert results[0].category == "Food"
    assert results[1].date == "2024-06-03"
    assert results[1].amount == 15.00
    assert results[1].category == "Utilities"