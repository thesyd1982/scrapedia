from models.client import Client
from models.individual import Individual
from models.address_builder import AddressBuilder

class IndividualClient(Client,Individual):

    def __init__(self, id_client,fname, lname, email, addr, tel):
        Client.__init__(id_client)
        Individual.__init__(addr, fname, lname, email,  tel)

    def order(self):
        pass


if __name__ == "__main__":
    adresse = AddressBuilder().build()
    fname = "Douakha"
    lname = "salah"
    tel = "0606060606"
    email="salah.yacin.douakha@gmail.com"
    contact = Individual(adresse)

    mcdonald = IndividualClient(1,adresse,fname, lname, email,  tel)
    print(mcdonald)
