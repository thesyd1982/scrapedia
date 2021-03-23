class Invoice:
    def __init__(self, company, client):
        self.invoice_lines = []
        self.company = company
        self.client = client

    def add_line(self, line):
        self.invoice_lines.append(line)

    def remove_line(self, line):
        self.invoice_lines.remove(line)


pass

if __name__ == '__main__':
    from models.category import Category
    from models.vat import Vat
    from models.product import Product
    from models.invoice_line import InvoiceLine
    from models.individual import Individual
    from models.individual_client import IndividualClient
    from models.address_builder import AddressBuilder


    cat = Category('Fruits', Vat.TAUX_REDUIT)

    banana = Product("16Xb51", "Banane plantin", 10, "sachet de 500g", cat, Vat.TAUX_REDUIT, "c'est de la bombe")

    il = InvoiceLine(banana, 2, 0.5)
    print(il)

    adresse = AddressBuilder().build()
    fn = "Douakha"
    ln = "salah"
    tel = "0606060606"
    mail = "salah.yacin.douakha@gmail.com"
    contact = Individual(fn, ln, adresse)

    mcdonald = IndividualClient(fn, ln, adresse, mail, tel)

    i = Invoice(mcdonald, contact)
    print(i)