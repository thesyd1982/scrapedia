from core.i_crud_repository import ICrudRepository
from core.i_repository import IRepository
from models.address import Address


class AddressRepository(IRepository):

    def __init__(self):
        self.addresses = [Address("34", "avenue de la bajatiere", "38100", "Grenoble", 'France'),
                          Address("19", "avenue de la bijpoune", "38400", "SMH", 'France'),
                          Address("45", "pageneuge", "38400", "donto", 'France')]

    def count(self):
        return self.addresses.count()
        pass

    def delete(self, entity):
        pass

    def delete_all(self, entities):
        pass

    def delete_by_id(self, id_entity):
        pass

    def exists_by_id(self, id_entity):
        return self.find_by_id(id_entity) is not None
        pass

    def find_all(self):
        return self.addresses
        pass

    def find_all_by_ids(self, entities_ids):
        pass

    def find_by_id(self, id_entity):
        return [e if e.id_address == id_entity else None for e in self.addresses][0]
        pass

    def save(self, entity):
        if not self.exists_by_id(entity.id_address):

            self.addresses.append(entity)
        else:
            self.addresses.remove(self.find_by_id(entity.id_address))
            self.addresses.append(entity)
        pass

    def save_all(self, entities):
        pass


pass
