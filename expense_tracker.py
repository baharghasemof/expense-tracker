expenses = [ ]

name = input("Expense name: ")
amount = float(input("Amount: "))
category = input("Category: ")

expense = [name, amount, category]

expenses.append(expense)

print("\n=== Expense information ===")
print(f"name        : {name}")
print(f"Amount      : {amount}")
print(f"Category    : {category}")

print("\ntotal expenses recorded: ", len(expenses))