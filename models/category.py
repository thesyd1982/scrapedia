from core.model import Model


class Category(Model):

    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_products(self):
        liste = ''
        for p in self.products:
            liste = liste + p.reference + ','
        liste = liste.strip(',')
        return liste

