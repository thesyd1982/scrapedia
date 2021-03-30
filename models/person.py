from abc import ABC
from core.model import Model


class Person(ABC, Model):

    def __init__(self, fname, lname, address=None, email=None, phone=None):
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.email = email
        self.address = address
        self.phone = phone
        # self.id_person = None



if __name__ == "__main__":
    pass
