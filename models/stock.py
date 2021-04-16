from models.category import Category
from models.product import Product
from models.vat import Vat
from core.model import Model


class Stock(Model):

    def __init__(self):
        super().__init__()
        self.stock_lignes = {}

    def add_stock_line(self, stock_line):

        if stock_line.reference in self.stock_lignes:
            self.stock_lignes[stock_line.reference].add_quantity(stock_line.quantity)
        else:
            self.stock_lignes[stock_line.reference] = stock_line

    def sub_stock_line(self,  stock_line):
        if stock_line.reference in self.stock_lignes:
            quantity = self.stock_lignes[stock_line.reference].quantity
            qty = stock_line.quantity

            if quantity - qty >= 0:
                quantity -= qty
                self.stock_lignes[stock_line.reference].quantity = quantity
            else:
                raise Exception('Quantité insuffisante')
        else:
            raise Exception("référence introuvable")


s = Stock()
cat_alim = Category('Fruits',
                    'Les Fruits des arbres ou des plantes')
banana = Product("16Xb51",
                 "Banane plantin",
                 10,
                 12,
                 'Kg',
                 'label rouge',
                 "sachet",
                 cat_alim,
                 Vat.TAUX_REDUIT,
                 "c'est de la bombe")

line = StockLine(banana.reference, 2, alert='warning')

try:
    s.add_stock_line(line)
    s.add_stock_line(line)
    s.sub_stock_line(line)

    print(s.get_stock_line(banana))
    # s.substract_stock_line(banana, 1)
except Exception as e:
    raise e

print(s)
