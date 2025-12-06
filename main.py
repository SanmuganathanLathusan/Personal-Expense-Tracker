from expenses import add_expense, view_expenses, view_summary

def menu():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. View Summary\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
