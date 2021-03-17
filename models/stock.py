from models.category import Category
from models.product import Product
from models.vat import Vat


class Stock:

    def __init__(self):
        self.lignes_stock = {}

    def add_product(self, product, qty=0):
        if product.reference in self.lignes_stock:
            self.lignes_stock[product.reference] += qty
        else:
            self.lignes_stock[product.reference] = qty

    def substract_product(self, product, qty=0):
        try:
            self.lignes_stock[product.reference] -= qty
        except:
            print("reference introuvable")


s = Stock()
cat_alim = Category('Fruits', Vat.TAUX_REDUIT)
banana = Product("16Xb51", "1234567891234", "Banane plantin", 1, cat_alim, "sachet de 500g", "c'est de la bombe")
s.add_product(banana, 2)
s.add_product(banana, 4)
s.substract_product("", 10)
print(s.__dict__)
