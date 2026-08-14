class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def show_info(self):
        print("Expense Name:", self.name)
        print("Amount:", self.amount)
        print("Category:", self.category)

    def is_expensive(self):
        return self.amount >= 50000

    def apply_discount(self):
        return self.amount * (1 - 50 / 100)

    def change_category(self, new_category):
        self.category = new_category


expenses = []

name = input("Expense name: ")
amount = float(input("Amount: "))
category = input("Category: ")

expense = Expense(name, amount, category)
expenses.append(expense)

print("\nLast expense:")
expenses[-1].show_info()

print("\n=== Testing Methods ===")

print("Is expensive:", expense.is_expensive())

print("Amount after 50% discount:", expense.apply_discount())

expense.change_category("Shopping")

print("\n=== Updated Expense ===")
expense.show_info()

print("\nTotal expenses recorded:", len(expenses))

print("\n=== All Expenses ===")

for expense in expenses:
    expense.show_info()