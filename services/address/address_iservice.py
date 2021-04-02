from abc import abstractmethod
from core.i_service import IService


class AddressIService(IService):

    def __init__(self, irepo=None):
        self.repo = irepo

    def set_repo(self, irepo):
        self.repo = irepo
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, item_id):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def update(self, item):
        pass

    @abstractmethod
    def delete(self, item):
        pass
