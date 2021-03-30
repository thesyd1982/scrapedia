from abc import ABC, abstractmethod

from core.i_repository import IRepository


class ICrudRepository(IRepository, ABC):

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def delete_all(self, entities):
        pass

    @abstractmethod
    def delete_by_id(self, id_entity):
        pass

    @abstractmethod
    def exists_by_id(self, id_entity):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_all_by_ids(self, entities_ids):
        pass

    @abstractmethod
    def find_by_id(self, id_entity):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def save_all(self, entities):
        pass


pass
