from core.model import Model
from utils.formater.formatings.oneline_formating import OnelineFormating


class Address(Model):

    def __init__(self, numero=None, voirie=None, ville=None, code_postal=None, pays=None):
        super().__init__()
        self.numero = numero
        self.voirie = voirie
        self.ville = ville
        self.code_postal = code_postal
        self.pays = pays


if __name__ == "__main__":
    a = Address()
    a.set_formating(OnelineFormating())
    print(a)
