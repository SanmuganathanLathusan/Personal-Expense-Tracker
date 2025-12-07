
# 📘 Personal Expense Tracker (Python)

A simple command-line Python application to track your daily expenses.
You can add expenses, view all records, and see a category-wise summary.
Data is stored locally in a JSON file.

---

## 🚀 Features

* ➕ Add a new expense (amount, category, description, date)
* 📄 View all saved expenses
* 📊 View expense summary by category
* 💾 Automatically saves data to `expenses.json`
* 🧩 Simple and beginner-friendly Python project
* 🖥️ Works on Windows, macOS, Linux

---

## 📂 Project Structure

```
expense_tracker/
│
├─ main.py           # Main application menu and flow
├─ expenses.py       # Functions for adding, viewing, summarizing expenses
├─ utils.py          # JSON load/save helpers
├─ expenses.json     # Auto-created storage file
└─ README.md         # Documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SanmuganathanLathusan/Personal-Expense-Tracker.git
cd Personal_Expense_Tracker
```

### 2. Run the app

```bash
python main.py
```

---

## 🧪 How to Use

### ▶️ Start Program

When you run the program, you will see:

```
1. Add Expense
2. View Expenses
3. View Summary
4. Exit
```

### ➕ Add an Expense

Enter:

* Category (Food, Transport, etc.)
* Amount
* Description
* Date (leave blank to auto-use today's date)

### 📄 View All Expenses

Shows all stored records in JSON.

### 📊 View Summary

Shows total spent **per category**.

---

## 📁 Data Storage

All expense data is stored in:

```
expenses.json
```

Example content:

```json
[
  {
    "category": "Food",
    "amount": 500,
    "description": "Lunch",
    "date": "2025-12-06"
  }
]
```

---

## 🛠️ Requirements

No external packages needed.
Runs with default Python installation (Python 3.8+ recommended).

---

## 💡 Future Improvements (Optional)

You can enhance the project by adding:

* CSV export
* Monthly reports
* GUI app using Tkinter
* Web dashboard using Flask
* Login system

---

## 🤝 Contributing

Pull requests are welcome!
If you find issues or have feature suggestions, feel free to open an issue.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---





