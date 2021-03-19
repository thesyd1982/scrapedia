class InvoiceLine:
    def __init__(self, qty, product):
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

pass
