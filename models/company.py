from address import Address
from core.model import Model
from models.individual import Individual


class Company(Model):

    def __init__(self, siret, name, address, contact=None):
        super().__init__()
        self.address = address
        self.name = name
        self.siret = siret
        self.contact = contact
        self.id_company = None

    def __str__(self):
        return f'\nCompany' \
               f'\n id_company: {self.id_company}' \
               f'\n siret: {self.siret}' \
               f'\n name: {self.name}' \
               f'{self.address}' \
               f'{self.contact}'


if __name__ == "__main__":
    a = Address("34", "avenue de la bajatiere", "38100", "Grenoble")
    c = Individual('Douakha', 'Sami', a)
    company = Company("145 678 901 21235", "Noobz", a, c)
    print(company)
