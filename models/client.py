from models.person import Person
from address_builder import AddressBuilder


class Client(Person):
    def __init__(self, fname, lname, email, address, tel, client_id, **kwargs):
        super().__init__(fname, lname, email, address, tel)

        self.client_id = client_id
        self.kwargs = kwargs
        for k, v in kwargs:
            self.k = v

    def __str__(self):
        return "Client({})".format(self.__dict__)


if __name__ == "__main__":
    #p = Person("toot")
    #print(p)
    adresse = AddressBuilder().build()
    c = Client("salah", "douakha", "salah.douhaka@gmail.com", adresse, '0606060606', 1)
    print(c)
