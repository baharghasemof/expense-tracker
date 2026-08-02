expenses = [ ]

name = input("Expense name: ")
amount = float(input("Amount: "))
category = input("Category: ")

expense = [name, amount, category]

expenses.append(expense)

print("\nlast expense: ")
print(expenses[-1])

print("\n=== Expense information ===")
print(f"name        : {name}")
print(f"Amount      : {amount}")
print(f"Category    : {category}")

print("\ntotal expenses recorded: ", len(expenses))

print("\n=== All Expenses ===")

for expense in expenses:
    print(expense)