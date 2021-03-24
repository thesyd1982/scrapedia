from core.model import Model

from utils.default_formater import DefaultFormater


class Address(Model):

    def __init__(self, numero=None, voirie=None, ville=None, code_postal=None, pays=None):
        self.numero = numero
        self.voirie = voirie
        self.ville = ville
        self.code_postal = code_postal
        self.pays = pays
        self.id_address = None

    # def __str__(self):
    #     return f'\nAddress' \
    #            f'\n  id_adresse: {self.__id_address}' \
    #            f'\n  voirie: {self.__voirie}' \
    #            f'\n  ville: {self.__ville}' \
    #            f'\n  code_postal: {self.__code_postal}' \
    #            f'\n  pays: {self.__pays}'

    # def __str__(self):
    #     return str(self.__dict__)
if __name__ == "__main__":
    a = Address("34", "avenue de la bajatiere", "38100", "Grenoble", 'France')

    for i in range(30):
        print(a.__repr__())
