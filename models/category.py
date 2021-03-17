class Category:

    def __init__(self, name, vat):

        self.name = name
        self.vat = vat
        self.products = []

    def __str__(self):
        return f'\nCategory ' \
               f'\n name: {self.name} ' \
               f'\n Vat: {self.vat}' \
               f'\n taux: {self.vat.value*100}%' \
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
class nimp:
    def __init__(self):
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start *= 2
        return self.start

    __call__ = __next__


pass


class A:
    def __init__(self):
        self.test = 0

    def __next__(self):
        self.test = self.test + 1
        return self.test

    def __iter__(self):
        return self

    __call__ = __next__


if __name__ == "__main__":

    def forIt(A, sentinel):
        return iter(A(), sentinel)


    for x in forIt(A, 5):
        print(x)
    cat_alim = Category("alimentaire", 5, 1)
