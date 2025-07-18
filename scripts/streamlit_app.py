import sys
import os


# Ensure the expense_tracker folder is in sys.path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
# expense_tracker_dir = os.path.join(parent_dir, "expense_tracker")
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import streamlit as st
from expense_tracker import services

st.title("Expense Tracker")

menu = ["Add Single Expense", "Bulk Upload (CSV)", "View Summary"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Single Expense":
    st.header("Add Single Expense")
    with st.form("single_expense_form"):
        date = st.text_input("Date (YYYY-MM-DD)")
        amount = st.text_input("Amount")
        category = st.text_input("Category")
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            try:
                amount_val = float(amount)
                services.add_expense(date=date, amount=amount_val, category=category)
                st.success("Expense added successfully!")
            except Exception as e:
                st.error(f"Failed to add expense: {e}")

elif choice == "Bulk Upload (CSV)":
    st.header("Bulk Upload Expenses")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        import tempfile
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        df.to_csv(temp_path.name, index=False)
        try:
            expenses = services.bulk_upload_expenses(temp_path.name)
            st.success(f"Successfully uploaded {len(expenses)} expenses from CSV.")
        except Exception as e:
            st.error(f"Failed to upload expenses: {e}")

elif choice == "View Summary":
    st.header("Expense Summary/Analysis")
    summary = services.get_summary()
    st.text(summary)