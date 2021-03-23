class InvoiceLine:
    def __init__(self, product, qty, promotion=0):
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

    def __str__(self):
        return f'InvoiceLine:\n name:{self.product.name}' \
               f'\n reference: {self.product.reference}' \
               f'\n price_ht: {self.price_ht}' \
               f'\n unit_price_ttc: {self.get_unit_price_ttc()}' \
               f'\n amount_vat: {self.get_amount_vat()}' \
               f'\n line_price_ht: {self.get_line_price_ht()}' \
               f'\n line_price_ttc : {self.get_line_price_ttc()}'


if __name__ == '__main__':
    from models.category import Category
    from models.vat import Vat
    from models.product import Product

    cat = Category('Fruits', Vat.TAUX_REDUIT)
    banana = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat, Vat.TAUX_REDUIT,"c'est de la bombe")

    il = InvoiceLine(banana, 2, 0.5)
    print(il)
