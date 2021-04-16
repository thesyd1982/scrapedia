from repositories.product_repository import ProductRepository
from services.stock.stock_iservice import StockIService


class StockService(StockIService):

    def __init__(self):
        """init the constructor"""
        super().__init__()

    def get_all(self):
        return self.repo.find_all()
        pass

    def get_by_id(self, item_id):
        return self.repo.find_by_id(item_id)
        pass

    def add(self, item, qty=1):
        if not (self.repo.is_exists_by_id(item.id_product)):
            self.repo.save(item)
        else:
            item.quantity += qty
            self.repo.save(item)
        pass

    def update(self, item):
        self.repo.save(item)
        pass

    def delete(self, item, qty=0):
        if self.repo.is_exists(item.id_product):
            product = self.repo.find_by_id(item.id_product)
            if product.quantity - qty >= 0:
                product.quantity -= qty
            else:
                raise Exception('Quantité insuffisante')
        else:
            raise Exception("référence introuvable")


pass

if __name__ == '__main__':
    from utils.formater.formatings.oneline_formating import OnelineFormating
    from models.product import Product
    from models.category import Category
    from models.vat import Vat

    repo = ProductRepository()
    ss = StockService()

    ss.set_repo(repo)
    cat = Category('Fruits', Vat.TAUX_REDUIT)
    cat.set_formating(OnelineFormating(['products','id_product']))
    p = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat,Vat.TAUX_REDUIT, 30, "c'est de la bombe")
    p.set_formating(OnelineFormating(['id_product', 'Category', 'products']))

    ss.add(p.set_formating(OnelineFormating(['id_product', 'Category', 'products'])))

    for i in ss.get_all():
        print(i.set_formating(OnelineFormating(['id_product', 'Category', 'products'])))

    ss.description = "tanto de la tanto"
    ss.update(p)
    print(f'\nprint the updated object: {p}')
