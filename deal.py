from csv_entity import CSVEntity
from csv import reader
from datetime import datetime

class Deal(CSVEntity):
    def __init__(self, date, name, price, savings, description):
        self.date = date
        self.name = name
        self.price = price
        self.savings = savings
        self.description = description

    def to_csv(self):
        return (self.date.isoformat(), self.name, self.price, self.savings, self.description)

    def get_key(self):
        return self.date.isoformat() + '_' + self.name

    @staticmethod
    def dict_from_csv(csv):
        deals = {}
        has_header = bool(csv.read(1))
        csv.seek(0)
        csv_reader = reader(csv)
        if has_header:
            next(csv_reader)
        for row in csv_reader:
            d = datetime.strptime(row[0], '%Y-%m-%d').date()
            deal = Deal(d, *row[1:])
            deals[deal.get_key()] = deal
        return deals
