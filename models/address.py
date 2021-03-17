class Address:
    countInstance = 0

    def __init__(self, numero='1', voirie='voirie', ville='ville', code_postal='code_postal', pays='pays'):
        self.__numero = numero
        self.__voirie = voirie
        self.__ville = ville
        self.__code_postal = code_postal
        self.__pays = pays
        self.__idAddress = Address.countInstance
        Address.countInstance += 1

    @staticmethod
    def get_counter_instance():
        return Address.countInstance

    def __str__(self):
        return "Address({} ,{} ,{} ,{} ,{}, {})".format(
            self.__idAddress, self.__numero, self.__voirie, self.__ville, self.__code_postal, self.__pays
        )

