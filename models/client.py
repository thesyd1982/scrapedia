from abc import ABC, abstractmethod
from core.model import Model


class Client(ABC, Model):
    def __init__(self):
        Model.__init__(self)
        self.invoices = []
        self.avoirs = []
        self.quotes = []

