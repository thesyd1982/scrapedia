from models.client import Client
from models.company import Company
from models.address_builder import AddressBuilder
from models.individual import Individual

class ProfessionalClient(Client, Company):
    def __init__(self,  siret , company_name, address,  contact):
        Client.__init__(self)
        Company.__init__(self, siret,  company_name, address, contact)

    def __str__(self):
        return "ProfessionalClient"+Client.__str__(self)+Company.__str__(self)

    def order(self):
        pass
pass

if __name__ == "__main__":
    adresse = AddressBuilder().build()
    company_name = "McDonalds"
    siret = "12345678945612"

    contact = Individual('Douakha','Sami', adresse)
    mcdonald = ProfessionalClient(siret, company_name, adresse, contact)

    print(mcdonald)
