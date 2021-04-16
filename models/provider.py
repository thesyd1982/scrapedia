from core.model import Model


class Provider(Model):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self


pass
