from core.model import Model


class StockLine(Model):
    def __init__(self, reference, quantity=0, alert=None):
        super().__init__()
        self.reference = reference
        self.quantity = quantity
        self.alert = alert

    def add_quantity(self, quantity):
        self.quantity += quantity

    def sub_quantity(self, quantity):
        self.quantity -= quantity
