from core.i_crud_repository import ICrudRepository


class ClientRepository(ICrudRepository):

    def count(self):
        pass

    def delete(self, entity):
        pass

    def delete_all(self, entities):
        pass

    def delete_by_id(self, id_entity):
        pass

    def exists_by_id(self, id_entity):
        pass

    def find_all(self):
        pass

    def find_all_by_ids(self, entities_ids):
        pass

    def find_by_id(self, id_entity):
        pass

    def save(self, entity):
        pass

    def save_all(self, entities):
        pass


pass