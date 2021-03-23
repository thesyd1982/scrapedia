from models.category import Category
from models.vat import Vat


class Product:
    def __init__(self, reference, name, price, packaging, category, vat, description=None, gencode=None):
        self.reference = reference
        self.gencode = gencode
        self.name = name
        self.price = price
        self.category = category
        self.packaging = packaging
        self.description = description
        self.vat = vat
        category.add_product(self)

    def __str__(self):
        return f'\nProduct' \
               f'\n reference: {self.reference}' \
               f'\n gencode: {self.gencode}' \
               f'\n name: {self.name}' \
               f'\n price: {self.price}€' \
               f'\n description: {self.description}' \
               f'\n packaging: {self.packaging}' \
               f'\n taux: {self.vat.value * 100}%'

    def set_category(self, category):
        category.add_product(self)
        self.category = category
        return self

    def get_category(self):
        return self.category


if __name__ == "__main__":
    cat = Category('Fruits', Vat.TAUX_REDUIT)
    banana = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat, "c'est de la bombe", Vat.TAUX_REDUIT)
    print(banana)
    print(cat)
