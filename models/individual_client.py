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
    fn = "Douakha"
    ln = "salah"
    tel = "0606060606"
    mail = "salah.yacin.douakha@gmail.com"
    contact = Individual(fn, ln, adresse)

    mcdonald = IndividualClient(fn, ln,adresse, mail, tel)
    print(mcdonald)
