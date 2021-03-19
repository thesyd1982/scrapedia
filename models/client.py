from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self):
          self.id_client = None

    def __str__(self):

        return f'\nClient' \
           f'\n id_client: {self.id_client}'

    @abstractmethod
    def order(self):
        pass

