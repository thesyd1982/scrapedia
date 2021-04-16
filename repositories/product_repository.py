from core.i_repository import IRepository
from models.category import Category
from models.product import Product
from models.vat import Vat


class ProductRepository(IRepository):

    def __init__(self):
        self.products = fixture()

    def count(self):
        return self.products.count()
        pass

    def delete(self, entity):
        if self.is_exists_by_id(entity.id_product):
            self.products.remove(entity)
        pass

    def delete_all(self, entities):
        for e in entities:
            self.delete(e)
        pass

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
    p1 = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat,Vat.TAUX_REDUIT, 10, "c'est de la bombe")
    p2 = Product("16Xb52", "Pasteque", 10, "piece", cat,Vat.TAUX_REDUIT, 10, "doudi aime")
    p3 = Product("16Xb53", "cerise", 10, "barquette de 500g", cat,Vat.TAUX_REDUIT, 10, "c'est chere")
    p4 = Product("16Xb54", "Poire", 10, "vrac", cat,Vat.TAUX_REDUIT, 10, "c'est pas bon")

    return [p1, p2, p3, p4]


pass
