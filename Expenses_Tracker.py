expenses = {}

def add_expense():
    date = input("Enter Date(YYYY-MM-DD): ")
    category = input("Enter Category(Food, Travel,..): ")
    amount = int(input("Enter Amount spent: "))

    if date not in expenses:
        expenses[date] = {} 

    if category in expenses[date]:
        expenses[date][category] += amount
    else:
        expenses[date][category] = amount

    print("Expenses are added Successfully!")

def view_expenses():
    if not expenses:
        print("No expenses are found")
    else:
        print("All Expenses: ")
        for date, categories in expenses.items():
            print(f"Date: {date}")
            for category, amount in categories.items():
                print(f"  {category}: {amount:.2f}")

def report_by_category():
    if not expenses:
        print("No expenses are found to report")
    else:
        category_totals = {}
        for categories in expenses.values():
            for category, amount in categories.items():
                category_totals[category] = category_totals.get(category, 0) + amount
        
        print("Category-wise Report: ")
        for category, total in category_totals.items():
            print(f"{category} : {total:.2f}")

while True:
    print("Expenses Tracker: ")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. View Report by Categories")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        report_by_category()
    elif choice == "4":
        print("Thank You for using the Expenses Tracker!")
        break
    else:
        print("Invalid choice, Please try again")
