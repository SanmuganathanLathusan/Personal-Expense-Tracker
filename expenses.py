import csv
from datetime import datetime
from utils import load_data, save_data

def get_user_file(username):
    return f"expenses_{username}.json"

def add_expense(username):
    print("\n--- Add New Expense ---")

    category = input("Category: ")
    amount = input("Amount: ")

    try:
        amount = float(amount)
    except ValueError:
        print("❌ Invalid amount.")
        return

    description = input("Description: ")
    date = input("Date (YYYY-MM-DD) or blank for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }

    file = get_user_file(username)
    data = load_data(file)
    data.append(expense)
    save_data(file, data)

    print("✅ Expense added successfully!")


def view_expenses(username):
    print("\n--- All Expenses ---")
    
    file = get_user_file(username)
    data = load_data(file)

    if not data:
        print("No expenses yet.")
        return

    for i, exp in enumerate(data, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | Rs.{exp['amount']} | {exp['description']}")


def view_summary(username):
    print("\n--- Expense Summary ---")

    file = get_user_file(username)
    data = load_data(file)

    if not data:
        print("No expenses yet.")
        return

    summary = {}

    for exp in data:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    for cat, amt in summary.items():
        print(f"{cat}: Rs.{amt}")


def export_csv(username):
    print("\n--- Exporting to CSV ---")

    file = get_user_file(username)
    data = load_data(file)

    if not data:
        print("❌ No expenses to export.")
        return

    csv_filename = f"expenses_{username}.csv"

    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])

        for exp in data:
            writer.writerow([exp["date"], exp["category"], exp["amount"], exp["description"]])

    print(f"✅ CSV exported successfully: {csv_filename}")
