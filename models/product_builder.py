from models.category import Category
from models.product import Product


class ProductBuilder:

    def __init__(self):
        self.product = Product()

    def set_name(self, name):
        self.product.name = name
        return self

    def set_reference(self, reference):
        self.product.reference = reference
        return self

    def set_buying_price(self, buying_price):
        self.product.buying_price = buying_price
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def set_category(self, category):
        category.add_product(self.product)
        self.product.category = category
        return self

    def set_unit(self, unit):
        self.product.unit = unit
        return self

    def set_gencode(self, gencode):
        self.product.gencode = gencode
        return self

    def set_brand(self, brand):
        self.product.brand = brand
        return self

    def set_packaging(self, packaging):
        self.product.packaging = packaging
        return self

    def set_vat(self, vat):
        self.product.vat = vat
        return self

    def set_description(self, description):
        self.product.description = description
        return self


    def get_category(self):
        return self.category

    def build(self):
        return self.product

    def __str__(self):
        return self.product.__str__()

if __name__ == "__main__":
    from models.unit import Unit
    from models.vat import Vat

    cat = Category('Fruits', Vat.TAUX_REDUIT)
    banana = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat, Vat.TAUX_REDUIT, 10, "c'est de la bombe")
    print(banana)
    print(cat)
