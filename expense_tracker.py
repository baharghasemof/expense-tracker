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
        print("Total Price:", self.total_price())

    def is_expensive(self):
        return self.total_price() >= 50000

    def apply_discount(self):
        return self.amount * (1 - 50 / 100)

    def change_category(self, new_category):
        self.category = new_category

    def total_price(self):
        return self.amount * self.quantity
        
expenses = []

continue_adding = "yes"

while continue_adding == "yes":

    name = input("Expense name: ")
    amount = float(input("Amount: "))
    quantity = int(input("Quantity: "))
    category = input("Category: ")

    expense = Expense( name, amount, quantity, category)
    expenses.append(expense)

    continue_adding = input("Add another expense? (yes/no): ")

print("\nLast expense:")
expenses[-1].show_info()

print("\n=== All Expenses ===")

total_expenses_price = 0

for expense in expenses:
    expense.show_info()
    total_expenses_price += expense.total_price()
    
print("\nTotal expenses recorded:", len(expenses))
print("Total purchase price: ", total_expenses_price)