class Budget:   
    def __init__(self, id, month, year):
        self.id = id
        self.month = month
        self.year = year

    def __repr__(self):
        return f"id: {self.id}, month: {self.month}, year: {self.year}"