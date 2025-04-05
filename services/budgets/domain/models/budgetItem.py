class BudgetItem:   
    def __init__(self, id, name, allocatedAmount, saving):
        self.id = id
        self.name = name
        self.allocatedAmount = allocatedAmount
        self.saving = saving


    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, allocatedAmount: {self.allocatedAmount}, saving: {self.saving}"