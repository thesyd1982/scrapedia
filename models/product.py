from models.category import Category
from core.model import Model


class Product(Model):

    def __init__(self, reference, name, price, packaging, category, vat, description=None, gencode=None):
        super().__init__()
        self.reference = reference
        self.name = name
        self.buying_price = buying_price
        self.price = price
        self.unit = unit
        self.brand = brand
        self.packaging = packaging
        self.category = category
        self.vat = vat
        self.description = description
        self.gencode = gencode


        category.add_product(self)

    def set_category(self, category):
        category.add_product(self)
        self.category = category
        return self

    def get_category(self):
        return self.category


if __name__ == "__main__":
    from models.unit import Unit
    from models.vat import Vat

    cat = Category('Fruits', Vat.TAUX_REDUIT)
    banana = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat, Vat.TAUX_REDUIT, 10, "c'est de la bombe")
    print(banana)
    print(cat)
