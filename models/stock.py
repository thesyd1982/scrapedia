from models.category import Category

from models.stock_line import StockLine

from core.model import Model


class Stock(Model):

    def __init__(self):
        super().__init__()
        self.stock_lignes = {}

    def add_stock_line(self, stock_line):

        if stock_line.reference in self.stock_lignes:
            self.stock_lignes[stock_line.reference].add_quantity(stock_line.quantity)
        else:
            self.stock_lignes[stock_line.reference] = stock_line

    def sub_stock_line(self, stock_line):
        if stock_line.reference in self.stock_lignes:
            quantity = self.stock_lignes[stock_line.reference].quantity
            qty = stock_line.quantity

            if quantity - qty >= 0:
                quantity -= qty
                self.stock_lignes[stock_line.reference].quantity = quantity
            else:
                raise Exception('Quantité insuffisante')
        else:
            raise Exception("référence introuvable")

    def get_stock_line(self, product):
        return self.stock_lignes.get(product.reference)


if __name__ == "__main__":
    from models.unit import Unit
    from models.vat import Vat
    from product_builder import ProductBuilder

    s = Stock()
    cat_alim = Category('Fruits', 'Les Fruits des arbres ou des plantes')

    product_builder = ProductBuilder()
    banana = product_builder \
        .set_name("Banane plantin") \
        .set_reference("16Xb51") \
        .set_category(cat_alim) \
        .set_vat(Vat.TAUX_REDUIT) \
        .set_buying_price(10) \
        .set_price(12) \
        .set_packaging("sachet de 500g") \
        .set_brand("banania") \
        .set_gencode("978020137962") \
        .set_unit(Unit.KG) \
        .set_description("c'est de la bombe") \
        .build()

    line = StockLine(banana.reference, 2, alert='warning')

    try:
        s.add_stock_line(line)
        s.add_stock_line(line)
        s.sub_stock_line(line)

        sl = s.get_stock_line(banana)

        print(sl)

    # s.substract_stock_line(banana, 1)
    except Exception as e:
        raise e
    # probleme d'ajout des lignes de stock Quantité anormale ######
    print(s)
