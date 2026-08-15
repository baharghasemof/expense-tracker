class Expense:
    def __init__(self, name, amount, quantity, category):
        self.name = name
        self.amount = amount
        self.quantity = quantity
        self.category = category

    def show_info(self):
        print( self.name)
        print("Amount:", self.amount)
        print("Quantity:", self.quantity)
        print("Category:", self.category)

    def is_expensive(self):
        return self.total_price() >= 50000

    def apply_discount(self):
        return self.amount * (1 - 50 / 100)

    def change_category(self, new_category):
        self.category = new_category

    def total_price(self):
        return self.amount * self.quantity
        
expenses = []

name = input("Expense name: ")
amount = float(input("Amount: "))
quantity = int(input("Quantity: "))
category = input("Category: ")

expense = Expense(name, amount, quantity, category)
expenses.append(expense)

print("\nLast expense:")
expenses[-1].show_info()

print("\n=== Testing Methods ===")

print("Is expensive:", expense.is_expensive())

print("Amount after 50% discount:", expense.apply_discount())

expense.change_category("Shopping")

print("Total price:", expense.total_price())

print("\n=== Updated Expense ===")
expense.show_info()

print("\nTotal expenses recorded:", len(expenses))

print("\n=== All Expenses ===")

for expense in expenses:
    expense.show_info()