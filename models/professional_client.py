from models.client import Client
from models.company import Company
from models.address_builder import AddressBuilder
from models.individual import Individual

class ProfessionalClient(Client, Company):
    def __init__(self, id_client, addr, company_name, contact, siret ):
        Client.__init__(self, id_client)
        Company.__init__(self, addr, company_name, siret, contact)

    def order(self):
        pass
pass

if __name__ == "__main__":
    adresse = AddressBuilder().build()
    name = "McDonalds"
    siret = "12345678945612"
    contact = Individual(adresse)

    mcdonald = ProfessionalClient(1,adresse, name, siret, contact)
    print(mcdonald)
