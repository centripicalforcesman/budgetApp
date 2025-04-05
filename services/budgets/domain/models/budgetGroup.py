class BudgetGroup:   
    def __init__(self, id, name, budgetItems):
        self.id = id
        self.name = name
        self.budgetItems = budgetItems
        
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, budgetItems: {self.budgetItems}"