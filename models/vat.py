from enum import Enum


class Vat(Enum):
    TAUX_NORMAL = 0.20
    TAUX_INTERMEDIAIRE = 0.10
    TAUX_REDUIT = 0.055
    TAUX_PARTICULIER=0.021


if __name__ == "__main__":
    print(Vat.TAUX_NORMAL.value)
    print(Vat.TAUX_INTERMEDIAIRE.value)
    print(Vat.TAUX_REDUIT.value)
