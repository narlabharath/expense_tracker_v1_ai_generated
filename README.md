# Expense Tracker v1 (AI Generated - Copilot)

This is a Python-based expense tracker project, set up with GitHub Actions for CI/CD.

# Expense Tracker CLI & Web UI

A simple, test-driven command-line and web application to track expenses, supporting single entry, bulk CSV upload, and summary analysis.

---

## Features

- **Add Single Expense:**  
  Enter date, amount, and category for each expense (CLI or Web UI).

- **Bulk Upload:**  
  Import multiple expenses from a CSV file (`date,amount,category`) (CLI or Web UI).

- **View Summary:**  
  See total expenses and breakdown by category (CLI or Web UI).

- **Web UI:**  
  User-friendly interface built with Streamlit for easy interaction.

- **Test Coverage:**  
  Core logic is covered by automated tests.

---

## Folder Structure

```
expense_tracker_v1_ai_generated/
│
├── expense_tracker/
│   ├── models.py      # Expense data model
│   ├── services.py    # Core logic (add, bulk upload, summary)
│   ├── utils.py       # Validation and CSV parsing
│   └── __init__.py
│
├── scripts/
│   └── main.py        # Command-line interface
│
├── tests/
│   └── test_services.py # Automated tests
│
└── .venv/             # Python virtual environment
```

---

## Getting Started

### 1. Clone the repository and navigate to the project folder.

### 2. Create and activate a virtual environment:

```sh
python -m venv .venv
# On Windows CMD:
.venv\Scripts\activate.bat
# On PowerShell:
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies (if any):

```sh
pip install -r requirements.txt
```
*(No external dependencies required for core features.)*


### 4. Run the CLI:

```sh
python scripts/main.py
```

### 5. Run the Web UI (Streamlit):

```sh
streamlit run scripts/streamlit_app.py
```

---


## Usage

### CLI
- **Add a single expense:**  
  Follow prompts for date (YYYY-MM-DD), amount, and category.
- **Bulk upload:**  
  Prepare a CSV file with columns: `date,amount,category`. Enter the file path when prompted.
- **View summary:**  
  Shows total and per-category expenses for the current session.

### Web UI (Streamlit)
- **Add a single expense:**  
  Use the sidebar to select "Add Single Expense" and fill out the form.
- **Bulk upload:**  
  Use the sidebar to select "Bulk Upload (CSV)", then upload your CSV file.
- **View summary:**  
  Use the sidebar to select "View Summary" to see totals and breakdowns.

---

## Running Tests

```sh
pytest
```

---

## Notes

- Expenses are stored in memory for the current session only.
- To persist data, extend the service layer to save/load from a file or database.

---

## Example CSV

```csv
date,amount,category
2024-06-01,10.00,Food
2024-06-02,20.50,Transport
```

---

## License

MIT License