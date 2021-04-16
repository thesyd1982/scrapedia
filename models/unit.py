from enum import Enum


class Unit(Enum):
    LITER = 'Liter'
    KG = 'Kg'
    PIECE = 'Piece'


if __name__ == "__main__":
    print(Unit.LITER.value)
    print(Unit.KG.value)
    print(Unit.PIECE.value)
