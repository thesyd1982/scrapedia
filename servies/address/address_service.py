from repositories.address_repository import AddressRepository
from servies.address.address_iservice import AddressIService


class AddressService(AddressIService):

    def __init__(self):
        super().__init__()

    def get_all(self):
        return self.repo.find_all()
        pass

    def get_by_id(self, item_id):
        return self.repo.find_by_id(item_id)
        pass

    def add(self, item):
        self.repo.save(item)
        pass

    def update(self, item):
        self.repo.save(item)
        pass

    def delete(self, item):
        self.repo.delete(item)
        pass


pass

if __name__ == '__main__':
    from utils.formater.formatings.oneline_formating import OnelineFormating
    from models.address import Address
    import uuid

    repo = AddressRepository()
    ads = AddressService()

    ads.set_repo(repo)

    a = Address()
    ads.add(a)

    for i in ads.get_all():
        print(i.set_formating(OnelineFormating()))

    a.code_postal = "8888"
    ads.update(a)
    print(f'\nprint the updated object: {a}')
