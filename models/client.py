from abc import ABC, abstractmethod
from core.model import Model


class Client(ABC, Model):
    def __init__(self):
        Model.__init__(self)
        self.id_client = None

    @abstractmethod
    def order(self):
        pass
