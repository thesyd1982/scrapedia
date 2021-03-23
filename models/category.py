class Category:

    def __init__(self, name, description):

        self.name = name
        self.description = description
        self.products = []

    def __str__(self):
        return f'\nCategory ' \
               f'\n name: {self.name} ' \
               f'\n description: {self.description}' \
               f'\n Products: [ {self.display_products()} ]'

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def display_products(self):
        liste = ''
        for p in self.products:
            liste = liste + p.reference+','
        liste = liste.strip(',')
        return liste
    pass
