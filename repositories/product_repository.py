from core.i_repository import IRepository
from models.category import Category
from models.product import Product
from models.vat import Vat
from models.product_builder import ProductBuilder
from models.unit import Unit


class ProductRepository(IRepository):

    def __init__(self):
        self.products = fixture()

    def count(self):
        return self.products.count()

    def delete(self, entity):
        if self.is_exists_by_id(entity.id_product):
            self.products.remove(entity)

    def delete_all(self, entities):
        for e in entities:
            self.delete(e)

    def delete_by_id(self, id_entity):
        entity = self.find_by_id(id_entity)
        if entity:
            self.products.remove(entity)
        pass

    def is_exists_by_id(self, id_entity):
        return self.find_by_id(id_entity) is not None
        pass

    def find_all(self):
        # TODO add the pagination
        return self.products
        pass

    def find_all_by_ids(self, entities_ids):
        pass

    def find_by_id(self, id_entity):
        return [e if e.id_product == id_entity else None for e in self.products][0]
        pass

    def save(self, entity):
        if not self.is_exists_by_id(entity.id_product):

            self.products.append(entity)
        else:
            self.products.remove(self.find_by_id(entity.id_product))
            self.products.append(entity)
        pass

    def save_all(self, entities):
        pass


pass


def fixture():
    cat = Category('Fruits', Vat.TAUX_REDUIT)
    product_builder = ProductBuilder()
    p = product_builder \
        .set_reference("16Xb51") \
        .set_gencode("978020137962") \
        .set_name("Banane") \
        .set_buying_price(0.88) \
        .set_price(1.48) \
        .set_brand("scb premium") \
        .set_description("c'est de la bombe") \
        .set_category(cat) \
        .set_vat(Vat.TAUX_REDUIT) \
        .set_packaging("sachet de 500g") \
        .set_unit(Unit.KG) \
        .build()

    p1 = ProductBuilder() \
        .set_reference("16Xb52") \
        .set_name("Pasteque") \
        .set_gencode("978020137975") \
        .set_buying_price(1.1) \
        .set_price(1.21) \
        .set_brand("McMelon") \
        .set_description("Le fruit que doudi aime") \
        .set_packaging("piece") \
        .set_vat(Vat.TAUX_REDUIT) \
        .set_category(cat) \
        .build()
    p2 = ProductBuilder() \
        .set_reference("16Xb53") \
        .set_name("Cerise") \
        .set_gencode("978020137998") \
        .set_buying_price(4.5) \
        .set_price(4.94) \
        .set_brand("pure") \
        .set_description("Le fruit que sarounette aime") \
        .set_packaging("barquette de 500g") \
        .set_vat(Vat.TAUX_REDUIT) \
        .set_category(cat) \
        .build()

    p3 = ProductBuilder() \
        .set_reference("16Xb54") \
        .set_name("Poire") \
        .set_gencode("978020137999") \
        .set_buying_price(1.23) \
        .set_price(1.35) \
        .set_brand("edenia") \
        .set_description("Le fruit que sarounette aime") \
        .set_packaging("vrac") \
        .set_vat(Vat.TAUX_REDUIT) \
        .set_category(cat) \
        .build()

    return [p, p1, p2, p3]


pass
