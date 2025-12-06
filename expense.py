import json
from utils import load_data, save_data
from datetime import datetime

FILE = "expenses.json"

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    date = input("Date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    expense = {"category": category, "amount": amount, "description": description, "date": date}
    
    data = load_data(FILE)
    data.append(expense)
    save_data(FILE, data)
    print("Expense added successfully!")

def view_expenses():
    data = load_data(FILE)
    for exp in data:
        print(exp)

def view_summary():
    data = load_data(FILE)
    summary = {}
    for exp in data:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
    for cat, amt in summary.items():
        print(f"{cat}: ${amt}")
