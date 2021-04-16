from models.category import Category
from core.model import Model



class Product(Model):
    # , reference, name, price, packaging, category, vat, buying_price, brand, unit, description = None,
    # gencode = None
    def __init__(self):
        super().__init__()
        self.reference = None
        self.name = None
        self.buying_price = None
        self.price = None
        self.unit = None
        self.brand = None
        self.packaging = None
        self.category = None
        self.vat = None
        self.description = None
        self.gencode = None

    def set_category(self, category):
        category.add_product(self)
        self.category = category
        return self

    def get_category(self):
        return self.category


if __name__ == "__main__":
    from models.unit import Unit
    from models.vat import Vat
    from product_builder import ProductBuilder
    cat = Category('Fruits', Vat.TAUX_REDUIT)

    product_builder = ProductBuilder()
    banana = product_builder \
        .set_name("Banane plantin") \
        .set_reference("16Xb51") \
        .set_category(cat) \
        .set_vat(Vat.TAUX_REDUIT) \
        .set_buying_price(10) \
        .set_price(12) \
        .set_packaging("sachet de 500g") \
        .set_brand("banania") \
        .set_gencode("978020137962") \
        .set_unit(Unit.KG) \
        .set_description("c'est de la bombe")

    print(banana)
    print(cat)
