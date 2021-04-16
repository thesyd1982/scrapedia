from models.address import Address
from core.model import Model
from models.individual import Individual


class Company(Model):

    def __init__(self, siret, name, address, contact=None):
        super().__init__()
        self.address = address
        self.name = name
        self.siret = siret
        self.contact = contact




if __name__ == "__main__":
    a = Address("34", "avenue de la bajatiere", "38100", "Grenoble")
    c = Individual('Douakha', 'Sami', a)
    company = Company("145 678 901 21235", "Noobz", a, c)
    print(company.id_company)
