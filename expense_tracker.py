# Personal Expense Tracker

expenses = []

budget = float(input("Enter Monthly Budget: Rs. "))


# Add Expense
def add_expense():

    description = input("Enter Description: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (DD-MM-YYYY): ")

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    print("Expense Added Successfully!")


# View All Expenses
def view_expenses():

    if len(expenses) == 0:
        print("No Expenses Found")
        return

    print("\n===== ALL EXPENSES =====")

    count = 1

    for expense in expenses:

        print("\nExpense", count)
        print("Description :", expense["description"])
        print("Category :", expense["category"])
        print("Amount :", expense["amount"])
        print("Date :", expense["date"])

        count += 1


# Category Summary
def category_summary():

    summary = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, total in summary.items():
        print(category, ":", total)


# Budget Report
def budget_report():

    total_spent = 0

    for expense in expenses:
        total_spent += expense["amount"]

    remaining = budget - total_spent

    percentage = (total_spent / budget) * 100

    print("\n===== BUDGET REPORT =====")
    print("Budget :", budget)
    print("Total Spent :", total_spent)
    print("Remaining :", remaining)
    print("Used :", round(percentage, 2), "%")

    if percentage >= 100:
        print("Budget Exceeded!")

    elif percentage >= 80:
        print("Warning: Budget Above 80%")

    else:
        print("Budget Under Control")


# Main Menu
while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        budget_report()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")