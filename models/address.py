class Address:

    def __init__(self, numero=None, voirie=None, ville=None, code_postal=None, pays=None):
        self.__numero = numero
        self.__voirie = voirie
        self.__ville = ville
        self.__code_postal = code_postal
        self.__pays = pays
        self.__id_address = None

    @staticmethod
    def get_counter_instance():
        return Address.countInstance

    def __str__(self):
        return f'\nAddress' \
               f'\n  id_adresse: {self.__id_address}' \
               f'\n  voirie: {self.__voirie}' \
               f'\n  ville: {self.__ville}' \
               f'\n  code_postal: {self.__code_postal}' \
               f'\n  pays: {self.__pays}'


if __name__ == "__main__":
    a = Address("34", "avenue de la bajatiere", "38100", "Grenoble",'France')

    print(a)
