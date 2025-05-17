class Budget:   
    def __init__(self, id, month, year, budgetGroups):
        self.id = id
        self.month = month
        self.year = year
        self.budgetGroups = budgetGroups

    def __repr__(self):
        return f"id: {self.id}, month: {self.month}, year: {self.year}, budgetGroups: {self.budgetGroups}"
    
    def serialize(self):
        return {"id": self.id,
                "month": self.month,
                "year": self.year}