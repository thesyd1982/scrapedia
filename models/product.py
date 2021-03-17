from models.category import Category
from models.vat import Vat


class Product:
    def __init__(self, reference, gencode, name, price, category, packaging, description):
        self.reference = reference
        self.gencode = gencode
        self.name = name
        self.price = price
        self.category = category
        self.packaging = packaging
        self.description = description
        category.add_product(self)

    def __str__(self):
        return f'\nProduct' \
               f'\n reference: {self.reference}' \
               f'\n gencode: {self.gencode}' \
               f'\n name: {self.name}' \
               f'\n price: {self.price}€' \
               f'\n description: {self.description}' \
               f'\n packaging: {self.packaging}' \

    def set_category(self, category):
        category.add_product(self)
        self.category = category
        return self

    def get_category(self):
        return self.category

if __name__ == "__main__":
    cat_alim = Category('Fruits', Vat.TAUX_REDUIT)
    banana = Product("16Xb51", "1234567891234", "Banane plantin", 1, cat_alim, "sachet de 500g", "c'est de la bombe")
    print(banana)
    print(cat_alim)
