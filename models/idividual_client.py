from models.client import Client
from models.individual import Individual
from models.address_builder import AddressBuilder


class IndividualClient(Client, Individual):

    def __init__(self, fname, lname, address, email=None, phone=None):
        Client.__init__(self)
        Individual.__init__(self, fname, lname, address, email, phone)

    def __str__(self):
        return "IndividualClient"+Client.__str__(self)+Individual.__str__(self)

    def order(self):
        pass


if __name__ == "__main__":
    adresse = AddressBuilder().build()
    fname = "Douakha"
    lname = "salah"
    phone = "0606060606"
    email = "salah.yacin.douakha@gmail.com"
    contact = Individual(fname, lname, adresse)

    mcdonald = IndividualClient( fname, lname,adresse, email, phone)
    print(mcdonald)
