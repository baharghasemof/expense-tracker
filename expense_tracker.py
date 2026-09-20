class Expense:
    def __init__(self, name, amount, quantity, category):
        self.name = name
        self.amount = amount
        self.quantity = quantity
        self.category = category

    def show_info(self):
        print(self.name)
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

def add_expense():
    continue_adding = "yes"

    while continue_adding == "yes":

        while True:
            name = input("Expense name: ").strip()
            if name:
                break
            else:
                print("Expense name cannot be empty.")
        while True:
            try:
                amount = float(input("Amount: "))
                if amount > 0:
                    break
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount! Please enter a valid number.")
        while True:
            try:
                quantity = int(input("Quantity: "))
                if quantity > 0:
                    break
                else:
                    print("quantity must be positive.")
            except ValueError:
                print("Invalid quantity! Please enter a number.")
        category = input("Category: ")
    
        expense = Expense(name, amount, quantity, category)
        expenses.append(expense)

        continue_adding = input("Add another expense? (yes/no): ").strip().lower()

def show_expenses():
    print("\n=== All Expenses ===")

    total_expenses_price = 0

    for i, expense in enumerate(expenses,start=1):
    
        print(f"\n{i}. {expense.name}")
        print("   Amount:", expense.amount)
        print("   Quantity:", expense.quantity)
        print("   Category:", expense.category)
        print("   Total Price:", expense.total_price())
    
        print()
        total_expenses_price += expense.total_price()
    
    print("\nTotal expenses recorded:", len(expenses))
    print("Total purchase price:",     total_expenses_price)

def edit_expense():
    continue_editing = input("Do you want to edit an expense? (yes/no): "
    ).strip().lower()

    while continue_editing == "yes":
        while True: 
            try:
                expense_number = int(input("\nWhich expense do you want to edit?")
                )
        
                if 1 <= expense_number <= len(expenses):
                    break
                else:
                    print(
                        f"Please enter a number between 1 and {len(expenses)}."
                        )
                
            except ValueError:
                    print("Invalid choice! Please enter a number.")
            
        index = expense_number - 1
        selected_expense = expenses[index]

        print("\nSelected expense:")
        selected_expense.show_info()

        while True:

            print("\nWhat do you want to edit?")
            print("1. Name")
            print("2. Amount")
            print("3. Quantity")
            print("4. Category")
        
            try:
                choice = int(input("Enter your choice: "))
    
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please choose a number between 1 and 4.")

            except ValueError:
                print("Invalid choice! Please enter a number.")
        
        if choice == 1:

            while True:
                new_name = input("New name: ").strip()

                if new_name:
                    selected_expense.name = new_name
                    break
                else:
                    print("Name cannot be empty.")
            
        elif choice == 2:

            while True:
                try:
                    new_amount = float(input("New amount: "))

                    if new_amount > 0:
                        selected_expense.amount = new_amount
                        break
                    else:
                        print("Amount must be positive.")
    
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
            
        elif choice == 3:

            while True:
                try:
                    new_quantity = int(input("New quantity: "))

                    if new_quantity > 0:
                        selected_expense.quantity = new_quantity
                        break
                    else:
                        print("Quantity must be positive.")

                except ValueError:
                    print("Invalid quantity! Please enter a number.")
            
        elif choice == 4:

            new_category = input("New category: ").strip()

            selected_expense.category = new_category
    
        print("\n=== Updated Expenses ===")

        for i, expense in enumerate(expenses, start=1):
            print(f"\n{i}. {expense.name}")
            print("   Amount:", expense.amount)
            print("   Quantity:", expense.quantity)
            print("   Category:", expense.category)
            print("   Total Price:", expense.total_price()) 
    
        continue_editing = input("\nEdit another expense? (yes/no):").strip().lower()
    
    print("\nEdit finished.")

def delete_expense():
    continue_deleting = input("\nDo you want to delete an expense? (yes/no): "
    ).strip().lower()

    while continue_deleting == "yes":
        while True:
            try:
                expense_number = int(input("\nWhich expense do you want to delete?")
                )
            
                if 1 <= expense_number <= len(expenses):
                    break
                else:
                    print(
                    f"Please enter a number between 1 and {len(expenses)}."
                    )
                
            except ValueError:
                print("Invalid choice! ‏Please enter a number.")
            
        index = expense_number - 1
        selected_expense = expenses[index]
    
        print("\nSelected expense: ")
        selected_expense.show_info()
    
        confirmation = input(
        "\nAre you sure you want to delete this expense? (yes/no): "
        ).strip().lower()
        
        if confirmation == "yes":
            deleted_expense = expenses.pop(index)
            print("\nExpense deleted successfully.")
        
            print("\nDeleted expense: ")
            deleted_expense.show_info()
        else:
            print("\nExpense was not deleted.")
           
        print("\n=== All Expenses After Deletion ===")

        for i, expense in enumerate(expenses, start=1):
            print(f"\n{i}. {expense.name}")
            print("   Amount:", expense.amount)
            print("   Quantity:", expense.quantity)
            print("   Category:", expense.category)
            print("   Total Price:", expense.total_price())

        continue_deleting = input(
            "\nDelete another expense? (yes/no): "
        ).strip().lower()

    print("\nDelete finished.")

def search_expense():
    continue_searching = input("\nDo you want to search for an expense? (yes/no): "
    ).strip().lower()

    while continue_searching == "yes":

        search_term = input("\nWhat do you want to search for? ").strip().lower()
            
        search_results = []
                
        for expense in expenses:           
            if search_term in expense.name.lower():
                search_results.append(expense)
                    
        if len(search_results) == 0:
            print("SORRY! Your Search Not Found.")
        else: 
            for i, expense in enumerate(search_results, start=1):
                print(f"\n{i}. {expense.name}")

            try:
                search_choice = int(input("Which expense do you want to see? "))
                if 1 <= search_choice <= len(search_results):
                    index = search_choice - 1
                    selected_expense = search_results[index]
                
                    print("\nSelected Expense: ")
                    selected_expense.show_info()
                            
                else:
                    print("Invalid expense number.")
                            
            except ValueError:
                print("Please enter a valid number.")    
            
        continue_searching = input("\nDo you want to search again? (yes/no): "
        ).strip().lower()    
        
        
def main():
    while True:
        print("\n~ Main Menu ~")
        print("1. Add Expense")
        print("2. Show All")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            edit_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            search_expense()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Please enter a valid number.")
            
main()