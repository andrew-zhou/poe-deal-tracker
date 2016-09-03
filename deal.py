from csv_entity import CSVEntity

class Deal(CSVEntity):
    def __init__(self, date, name, price, savings, description):
        self.date = date
        self.name = name
        self.price = price
        self.savings = savings
        self.description = description

    def to_csv(self):
        return (self.date.isoformat(), self.name, self.price, self.savings, self.description)
