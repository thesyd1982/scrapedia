from models.person import Person
from models.address_builder import AddressBuilder

class Individual(Person):
    def __init__(self, addr, fname='fname', lname='lname', email='email@exemple.fr',  tel='0476900900'):
        super().__init__(fname, lname, email, addr, tel)
