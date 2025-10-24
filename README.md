# 💸 Python Expense Tracker

A simple **command-line Expense Tracker** built using **Python**.  
Keep track of your daily spending, categorize expenses, and calculate your total — all from the terminal!

---

## 🧠 Overview

This project helps you **manage your expenses easily**.  
You can add expenses, categorize them (like food, travel, shopping), view all records, and see your total spending.

It’s perfect for **Python beginners** learning about loops, lists, functions, and dictionaries.

---

## 🚀 Features

✅ Add expenses with amount and category  
✅ View all recorded expenses  
✅ Calculate total spending  
✅ Simple menu-driven interface  
✅ Beginner-friendly code (no external libraries needed)

---

## 🧾 Example Output

<<< Your Expenses Tracker >>>

=== Expense Tracker ===

Add Expense

View Expenses

View Total Spending

Exit
Choose an option: 1
enter the ammount here: 250
Enter category (food, travel, shopping, etc.): food
item for food And The Ammount 250 Are Added ✅

Copy code
=== Expense Tracker ===

Add Expense

View Expenses

View Total Spending

Exit
Choose an option: 2
---All Expenses---

250 - food

120 - travel
💰 Total spending: ₹370

python
Copy code

---

## 🧩 Code (Main Script)

Save this code as **`expense_tracker.py`**

```python
expenses = []

print("<<< Your Expenses Tracker >>>")
# Author: SushantGiri
# GitHub: https://github.com/SushantGiri34

def add_expenses():
    ammount = int(input("enter the ammount here: "))
    category = input("Enter category (food, travel, shopping, etc.): ")
    expenses.append({"ammount": ammount, "category": category})
    print(f" iteam for {category} And The Ammount {ammount} Are Added ✅")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("---All Expenses---")
    for i, exp in enumerate(expenses, start=1):
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






🖥️ How to Run
Make sure Python 3 is installed.
👉 Download Python

Clone this repository or download as ZIP:

bash
Copy code
git clone https://github.com/SushantGiri34/Expense-tracker.git
cd expense-tracker
Run the script:

bash
Copy code
python expense_tracker.py
Use the menu to add, view, and calculate expenses 💰

🧰 Future Improvements
✨ Load saved data automatically on program start
✨ Filter expenses by category or date
✨ Add colored terminal output for better UX

🧑‍💻 Author
Sushant Giri
🌐 https://github.com/SushantGiri34

🪪 License
This project is open-source under the MIT License.
You can freely use, modify, and share the code.
