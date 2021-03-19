from abc import ABC

class Person(ABC):
    def __init__(self, fname, lname,address=None, email=None,  phone=None):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.address = address
        self.phone = phone
        self.id_person = None

    def __str__(self):
        return f'\nPerson' \
               f'\n  id_person: {self.id_person}' \
               f'\n  fist name: {self.fname}' \
               f'\n  last name: {self.lname}' \
               f'\n  email: {self.email}' \
               f'\n  phone: {self.phone}'\
               f'{self.address}'

if __name__ == "__main__":
    pass


