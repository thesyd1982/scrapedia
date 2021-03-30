from core.model import Model
from utils.formater.formatings.oneline_formating import OnelineFormating
from utils.formater.formatings.default_formating import DefaultFormating


class InvoiceLine(Model):
    def __init__(self, product, qty, promotion=0):
        super().__init__()
        self.product = product
        self.qty = qty
        self.price_ht = self.product.price * (1 - promotion)

        # if self.price_ht is None:
        #     self.price_ht = self.product.price*
        # else:
        #     self.price_ht = price_ht

    """
    Invoice line : product reference | product name | unit price | unit vat | price ttc |
    line price | line vat | line price ttc
    """

    def get_amount_vat(self):
        return self.product.vat.value * self.price_ht

    def get_unit_price_ttc(self):
        return self.get_amount_vat() + self.price_ht

    def get_line_price_ttc(self):
        return self.get_unit_price_ttc() * self.qty

    def get_line_price_ht(self):
        return self.price_ht * self.qty


if __name__ == '__main__':
    from models.category import Category
    from models.vat import Vat
    from models.product import Product

    cat = Category('Fruits', 'Ce que les arbres donne')
    banana = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat, Vat.TAUX_REDUIT.value, "c'est de la bombe")
    banana.set_formating(OnelineFormating(['category'], False))
    cat.set_formating(OnelineFormating(['products']))

    il = InvoiceLine(banana, 2, 0.5).set_formating(OnelineFormating())

    print(il)
