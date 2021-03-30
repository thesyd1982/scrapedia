from abc import ABC, abstractmethod
from core.model import Model


class Client(ABC, Model):
    def __init__(self):
        Model.__init__(self)
        self.id_client = None

    def __str__(self):
        return f'\nClient' \
               f'\n id_client: {self.id_client}'

    @abstractmethod
    def order(self):
        pass
