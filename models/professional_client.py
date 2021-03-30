from models.client import Client
from models.company import Company
from models.address_builder import AddressBuilder
from models.individual import Individual


class ProfessionalClient(Client, Company):
    def __init__(self, siret, company_name, address, contact):
        Client.__init__(self)
        Company.__init__(self, siret, company_name, address, contact)


    def order(self):
        pass


pass

if __name__ == "__main__":
    addr = AddressBuilder().build()
    name = "McDonalds"
    s = "12345678945612"

    c = Individual('Douakha', 'Sami', addr)
    mcdonald = ProfessionalClient(s, name, addr, c)

    print(mcdonald)
