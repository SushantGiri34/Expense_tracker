expenses = []

print("<<< Your Expenses Tracker >>>")
#sushantgiri
def add_expenses():
    ammount = int(input("enter the ammount here: "))
    category = input("Enter category (food, travel, shopping, etc.): ")
    expenses.append({"ammount": ammount, "category": category})
    print(f" iteam for {category} And The Ammount {ammount} Are Added ✅")
#https://github.com/SushantGiri34
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("---All Expenses---")
    for i, exp in enumerate(expenses, start= 1):
        print(f"{i}. {exp['ammount']} - {exp['category']}")

def view_total():
    total = sum(ex['ammount'] for ex in expenses)
    print(f"💰 Total spending: ₹{total}")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expenses()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("⚠ Invalid choice. Try again.")