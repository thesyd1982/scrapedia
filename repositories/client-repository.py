from core.i_crud_repository import ICrudRepository
from models.address_builder import AddressBuilder
from models.individual import Individual
from models.individual_client import IndividualClient
from models.professional_client import ProfessionalClient


class ClientRepository(ICrudRepository):

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

    def exists_by_id(self, id_entity):
        pass

    def find_all(self):
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
    contact = Individual(fn, ln, adresse)

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

    return [indiv1, pro, indiv2]
