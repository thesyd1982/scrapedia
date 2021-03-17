from address import Address


class Company:

    def __init__(self, addr, name, siret, contact):
        self.address = addr
        self.name = name
        self.siret = siret
        self.contact = contact

    def __str__(self):
        return "siret: {} \n {},{},{}".format(self.siret, self.name, self.address.__str__(), self.contact.__str__())


if __name__ == "__main__":
    a = Address("34", "avenue de la bajatiere", "38100", "Grenoble")

    company = Company(a, "Noobz", "145 678 901 21235", "contact")
