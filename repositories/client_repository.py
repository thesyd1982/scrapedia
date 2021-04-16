from core.i_repository import IRepository
from models.address_builder import AddressBuilder
from models.individual import Individual
from models.individual_client import IndividualClient
from models.professional_client import ProfessionalClient


class ClientRepository(IRepository):

    def __init__(self):
        self.clients = fixture()

    def count(self):
        pass

    def delete(self, entity):
        pass

    def delete_all(self, entities):
        pass

    def delete_by_id(self, id_entity):
        pass

    def is_exists_by_id(self, id_entity):
        pass

    def find_all(self):
        return self.clients
        pass

    def find_all_by_ids(self, entities_ids):
        pass

    def find_by_id(self, id_entity):
        pass

    def save(self, entity):
        pass

    def save_all(self, entities):
        pass


pass


def fixture():
    adresse = AddressBuilder().build()
    fn = "Douakha"
    ln = "salah"
    tel = "0606060606"
    mail = "salah.yacin.douakha@gmail.com"

    indiv1 = IndividualClient(fn, ln, adresse, mail, tel)

    addr = AddressBuilder().build()
    name = "McDonalds"
    s = "12345678945612"

    c = Individual('Douakha', 'Sami', addr)
    pro = ProfessionalClient(s, name, addr, c)

    adresse = AddressBuilder().build()
    fn = "Chovin"
    ln = "antoine"
    tel = "0606060606"
    mail = "antoine.chovin@gmail.com"

    indiv2 = IndividualClient(fn, ln, adresse, mail, tel)

    return [indiv1,pro, indiv2]
