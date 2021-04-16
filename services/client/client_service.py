from services.client.client_iservice import ClientIService
from repositories.client_repository import ClientRepository


class ClientService(ClientIService):

    def __init__(self):
        """init the constructor"""
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

    repo = ClientRepository()
    clientService = ClientService()

    clientService.set_repo(repo)

    # adresse = AddressBuilder().build()
    # fn = "Douakha"
    # ln = "salah"
    # tel = "0606060606"
    # mail = "salah.yacin.douakha@gmail.com"
    #
    # indiv1 = IndividualClient(fn, ln, adresse, mail, tel)
    #
    # client = indiv1
    #
    # clientService.add(client)

    for i in clientService.get_all():
        print(i.set_formating(OnelineFormating()))

    # client.name = "38000"
    # clientService.update(client)
