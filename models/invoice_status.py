from enum import Enum


class InvoiceStatus(Enum):

    UNPAYED = 'UNPAYED'
    PAYED = 'PAYED'
    IN_PROGRESS = 'IN_PROGRESS'


if __name__ == "__main__":
    print(InvoiceStatus.UNPAYED.value)
    print(InvoiceStatus.PAYED.value)
    print(InvoiceStatus.IN_PROGRESS.value)