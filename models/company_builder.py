from core.model import Model
from models.copany import Company


class CompanyBuilder(Model):
    def __init__(self):
        self.__company = Company()

    def get_numero(self):
        return self.__address.numero

    def set_numero(self, numero):
        self.__address.numero = numero

    def get_voirie(self):
        return self.__address.voirie

    def set_voirie(self, voirie):
        self.__address.voirie = voirie
        return self

    def get_ville(self):
        return self.__address.ville

    def set_ville(self, ville):
        self.__address.ville = ville
        return self

    def get_code_postal(self):
        return self

    def set_code_postal(self, code_postal):
        self.__address.code_postal = code_postal
        return self

    def get_pays(self):
        return self.__address.pays

    def set_pays(self, pays):
        self.__address.pays = pays
        return self

    def build(self):
        return self.__address
