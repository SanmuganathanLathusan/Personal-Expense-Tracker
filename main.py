from auth import login_user, register_user
from expenses import add_expense, view_expenses, view_summary, export_csv

def main_menu(username):
    while True:
        print(f"\n===== EXPENSE TRACKER ({username}) =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Export to CSV")
        print("5. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(username)
        elif choice == "2":
            view_expenses(username)
        elif choice == "3":
            view_summary(username)
        elif choice == "4":
            export_csv(username)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def start():
    while True:
        print("\n===== WELCOME =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = login_user()
            if username:
                main_menu(username)

        elif choice == "2":
            username = register_user()
            if username:
                main_menu(username)

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    start()
