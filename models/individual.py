from models.person import Person


class Individual(Person):
    def __init__(self, fname, lname, address, email=None, phone=None):
        super().__init__(fname, lname, address, email, phone)
