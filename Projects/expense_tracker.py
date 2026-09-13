class ExpenseTracker:
    def __init__(self,owner):
        self.owner=owner
        self.expenses=[]
    
    def add_expenses(self, category: str, amount: float, description: str = ""):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.expenses.append({"category": category, "amount": amount, "description": description})
        print("Expense added successfully")

    def get_total(self)->float:
        if len(self.expenses)==0:
            print("There is no expenses recorded.")
            return 0.0
        total=0
        for item in self.expenses:
            total+=item["amount"]
        return total
    
    def get_highest_expenses(self):
        if not self.expenses:
            return None
        highest=self.expenses[0]
        for item in self.expenses:
            if item["amount"]>highest["amount"]:
                highest=item
        return highest
    
    def filter_by_category(self, category: str)->None:
        filtered_category = [expense for expense in self.expenses if expense["category"].lower() == category.lower()]
        return filtered_category
        
    
tracker = ExpenseTracker("DK")
tracker.add_expenses("Food", 150.0, "Lunch")
tracker.add_expenses("Transport", 50.0, "Bus")
tracker.add_expenses("Food", 200.0, "Dinner")

print("Total Spent:", tracker.get_total())
print("Highest:", tracker.get_highest_expenses())
print("Food only:", tracker.filter_by_category("food"))
       

