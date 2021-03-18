from abc import ABC
from models.address import Address

class Person(ABC):
    def __init__(self, fname='fname', lname='lname', email='email@exemple.fr', addr=Address(), tel='0476900900'):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.address = addr
        self.tel = tel

    def __str__(self):
        return "Person('{}' '{}' '{}' '{}' '{}')".format(
            self.fname, self.lname, self.email, self.address, self.tel
        )


if __name__ == "__main__":
    pass


